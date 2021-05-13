n,m=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(m)]
c=[0]*-~n
id={}
for p,y in sorted(a,key=lambda x:x[1]):
    c[p]+=1
    id[y]=str(p).zfill(6)+str(c[p]).zfill(6)
for _,y in a:
    print(id[y])