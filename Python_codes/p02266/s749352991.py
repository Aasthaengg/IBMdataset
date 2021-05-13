data = input()
stack = []
lakes = []
for i, X in enumerate(data):
    if X == "\\":
        stack.append(i)
    elif X == "/":
        try:
            j = stack.pop()
        except IndexError:
            continue
        s = 0
        while True:
            if (not lakes) or lakes[-1][1][0] < j:
                break
            s += lakes[-1][0]
            lakes.pop()
        lakes.append([i - j + s, (j, i)])

text = [len(lakes)] + [L[0] for L in lakes]
print(sum(text[1:]))
print(" ".join(list(map(str, text))))