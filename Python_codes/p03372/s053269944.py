from itertools import accumulate as acc
import sys

N,C=map(int,input().split())
a=[list(map(int,input().split())) for i in range(N)]

if N==1: print(max(0, a[0][1]-a[0][0], a[0][1]-(C-a[0][0]) ) ),sys.exit()

tmp=a[0][1]-a[0][0]
M=max(0,tmp)
l=[M]
for i in range(1,N):
    tmp+=a[i][1]-(a[i][0]-a[i-1][0])
    M=max(tmp,M)
    l.append(M)

tmp=a[N-1][1]-(C-a[N-1][0])
M=max(0,tmp)
r=[M]
for i in range(N-2,-1,-1):
    tmp+=a[i][1]-(a[i+1][0]-a[i][0])
    M=max(tmp,M)
    r.append(M)

r.reverse()

ans=max(l[0], r[0], l[0]-a[0][0]+r[1], l[N-1], r[N-1], r[N-1]-(C-a[N-1][0])+l[N-2])

for i in range(1,N-1):
    ans=max(ans, l[i], r[i], l[i]-a[i][0]+r[i+1], r[i]-(C-a[i][0])+l[i-1])

print(ans)