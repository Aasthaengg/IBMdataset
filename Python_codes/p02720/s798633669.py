k = int(input())

L = list(range(10))
i = 1
while len(L) <= k:
    Li = L[i]
    a = Li % 10
    for b in range(a - 1, a + 2):
        if b < 0 or b > 9:
            continue
        L.append(Li * 10 + b)
    i += 1

print(L[k])
