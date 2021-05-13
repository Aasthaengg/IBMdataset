s, t = input(), input()
a = len(s)
for i in range(len(s) - len(t) + 1):
    c = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            c += 1
    a = min(a, c)
print(a)     