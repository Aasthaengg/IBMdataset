n,m=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(m)]
c=[0]*-~n
id={}
for p,y in sorted(a,key=lambda x:x[1]):
    c[p]+=1
    id[y]=format(p,"06")+format(c[p],"06")
for _,y in a:
    print(id[y])