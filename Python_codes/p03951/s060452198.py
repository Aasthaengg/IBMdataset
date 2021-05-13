N = int(input())
s = input()
t = input()
c = 0
for o in range(len(s) + 1):
    d = 0
    for i in range(len(t)):
        if o + i >= len(s): break
        if s[o + i] == t[i]: d += 1
        else: break
    c = max(c, d)
print(len(s) + len(t) - c)
