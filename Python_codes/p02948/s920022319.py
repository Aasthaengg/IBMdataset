n,m=map(int,input().split())
ab=[list(map(int, input().split())) for _ in range(n)]
ab=list(sorted(ab, key=lambda x: x[0]))

import heapq
hq=[]
ans=0
j=0
for i in range(1, m+1):  # m-i日後を考える
    while (j<n) and (ab[j][0]<=i):
        heapq.heappush(hq, -ab[j][1])
        j+=1
    if len(hq):
        ans+=-heapq.heappop(hq)

print(ans)
