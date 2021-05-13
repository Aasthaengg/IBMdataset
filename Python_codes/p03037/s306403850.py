N,M=map(int,input().split())
L=[list(map(int,input().split()))for i in range(M)]
r=N
l=0
for i in range(M):
    l=max(l,L[i][0])
    r=min(r,L[i][1])
if r-l+1<0:
    print(0)
else:
    print(r-l+1)