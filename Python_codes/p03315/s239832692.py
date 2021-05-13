S = input()
n = 0
for i in range(4):
    if S[i] == "+":
        n += 1
    elif S[i] == "-":
        n -= 1
print(n)
