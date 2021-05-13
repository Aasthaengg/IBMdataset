n = int(input())
s = str(input())
m = 0
w = []
for j in s:
    w.append(j)
w = list(set(w))
for i in range(1,n):
    t = 0
    for h in w:
        if 1 <= s[:i].count(h) and 1 <= s[i:].count(h):
            t += 1
    if m < t:
        m = t
print(m)