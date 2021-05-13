h, w = map(int, input().split())
a = list(str(input()) for i in range(h))
s =[]
for j in range(w+2):
    s.append("#")
print(*s, sep="")
p = []
for k in range(h):
    p.append("#")
    p.append(a[k])
    p.append("#")
    print(*p, sep="")
    del p[:]
print(*s, sep="")