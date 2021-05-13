n,k=map(int,input().split())
alst=[0]+list(map(int,input().split()))

dis=[-1]*(n+1)
now=1
time=0
while 1 :
    if dis[now]>=0 : break
    dis[now]=time
    time+=1
    now=alst[now]

if time>k :
    print(dis.index(k))
else :
    head=dis[now]
    roop_unit=time-dis[now]
    work=(k-head)%roop_unit
    print(dis.index(head+work))