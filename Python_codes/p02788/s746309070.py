from bisect import bisect_right

N,D,A=list(map(int,input().split()))
monsters=[list(map(int,input().split())) for _ in range(N)]

monsters.sort(key=lambda x: x[0])
xlst=[x for x,_ in monsters]

delta=[0]*(N+1)
csum=0

ans=0

for i in range(N):
    xi,hi=monsters[i]
    csum+=delta[i]
    hi-=csum

    if hi<=0:
        continue

    cnt=(hi+A-1)//A
    ans+=cnt

    csum+=A*cnt
    right=bisect_right(xlst,xi+2*D)
    delta[right]-=A*cnt

print(ans)