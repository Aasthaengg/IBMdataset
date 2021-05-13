N,M=map(int,input().split())
L=-10**9
R=+10**9
for _ in range(M):
    l,r=map(int,input().split())
    L=max(L,l)
    R=min(R,r)
print(max(0,R-L+1))