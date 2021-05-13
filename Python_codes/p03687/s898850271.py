import math
s = input()
m = len(s)
for i in range(26):
    c = chr(i+ord('a'))
    t = s
    for j in range(len(t)):
        if t.count(c) == len(t):
            m = min(m, j)
        u = ''
        for k in range(len(t)-1):
            if t[k+1] == c:
                u += c
            else:
                u += t[k]
        t = u
print(m)
