a,b,M=map(int,input().split())
*A,=map(int,input().split())
*B,=map(int,input().split())
xyc=[list(map(int,input().split()))for _ in range(M)]

ans=min(A)+min(B)
for x,y,c in xyc:
    ans=min(ans,A[x-1]+B[y-1]-c)
print(ans)