n = int(input())

t = []

for i in range(n):
    s = list(input())
    s.sort()
    t.append(s)

t.sort()

s = 0
c = 0
l = []

for i in range(n):
    if t[i] == l:
        c += 1
    else:
        s += c * (c+1) // 2
        c = 0
        l = t[i]

if c > 0:
    s += c * (c+1) // 2

print(s)
