n = int(input())
l = [list(input().split()) for i in range(n)]
s,p = [list(i) for i in zip(*l)]
p = [int(i) for i in p]
z = list(set(s))
z.sort()
m = list(p)
m.sort(reverse = True)
l = []
 
k = 0
for i in range(len(z)):
    l.append(k)
    k += 200
 
o = []
for i in range(n):
    w = l[z.index(s[i])]
    w += m.index(p[i])
    o.append(w)
 
r = list(o)
r.sort()
for i in range(n):
    print(o.index(r[i]) + 1) 