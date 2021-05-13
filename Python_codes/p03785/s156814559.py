N,C,K=map(int,input().split())
T=[int(input()) for _ in range(N)]
T.sort()

ans=0
wait=[]
for i in range(N):
    t=T[i]
    if len(wait)>0 and t-wait[0]>K:
        ans+=1
        wait=[]
    wait.append(t)
    if len(wait)==C:
        ans+=1
        wait=[]
if len(wait)>0:
    ans+=1
print(ans)