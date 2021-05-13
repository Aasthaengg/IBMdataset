n = int(input())
sp = []
for i in range(n):
    s,p = map(str, input().split())
    sp.append((s,int(p)))
sp1 = tuple(sp)
sp = sorted(sp, key=lambda x:(x[0],-x[1]))
for h in sp:
    print(sp1.index(h)+1)