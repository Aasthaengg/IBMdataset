n,k=map(int,input().split())
A=list(map(int,input().split()))

for i in range(n):
    A[i]-=1

ans=0
hub_city=0
visited=[-1]*n
now=0
cnt_warp=0
loop_cnt=0
first_visit_hub_city=0

for i in range(n):
    if visited[now]>-1:
        hub_city=now
        first_visit_hub_city=visited[now]
        loop_cnt=cnt_warp-first_visit_hub_city
        break
    else:
        visited[now]=cnt_warp
    
    now=A[now]
    cnt_warp+=1

idoukaizu=min(first_visit_hub_city+(k-first_visit_hub_city)%loop_cnt,k)

now=0
for i in range(idoukaizu):
    now=A[now]

print(now+1)