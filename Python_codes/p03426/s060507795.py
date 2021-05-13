h,w,d=map(int,input().split())

a={}
for y in range(h):
    tmp=list(map(int,input().split()))

    for x,v in enumerate(tmp):
        a[v]=(y,x)

dis=[0]*(h*w+1)

#dis[j]=j%dからjまでのコスト

for i in range(1,h*w+1):
    if i>d:
        bk=a[i-d]
        nx=a[i]
        dis[i]=dis[i-d]+abs(bk[0]-nx[0])+abs(bk[1]-nx[1])

q=int(input())
ans=[]
for _ in range(q):
    start,goal=map(int,input().split())
    ans.append(dis[goal]-dis[start])

for item in ans:
    print(item)



