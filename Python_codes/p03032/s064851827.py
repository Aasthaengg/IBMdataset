n,k = map(int,input().split())
v = list(map(int,input().split()))
import bisect

ans=0
minnk = min(n,k)
for r in range(minnk+1):
    for l in range(minnk+1-r):
        sute = k-(r+l)
        
        temoti = sorted(v[:l] +v[n-r:])
        n_nega = bisect.bisect(temoti,0)
        score = sum(temoti[min(n_nega,sute):])

        if ans<score:
            ans=score
print(ans)   