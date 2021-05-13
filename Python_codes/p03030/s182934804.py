n = int(input())
s = []
p = [0] * 101
d = {}
for i in range(n):
    a,b = input().split()
    b = int(b)
    s.append(a)
    p[b] = i+1
    if a in list(d.keys()):
        d[a].append(b)
        continue
    d[a] = [b]
s = sorted(set(s))
for i in s:
    c = sorted(d[i],reverse=True)
    for j in c:
        print(p[j])
