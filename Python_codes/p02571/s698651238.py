s = input()
t = input()

S = len(s)
T = len(t)

x = len(t)
for i in range(S - T + 1):
    y = 0
    for j in range(T):
        if t[j] != s[i + j]:
            y += 1
    x = min(x, y)

print(x)