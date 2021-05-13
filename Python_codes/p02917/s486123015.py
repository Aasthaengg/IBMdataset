N,*B,=open(0).read().split()
N=int(N)
B=list(map(int,B))
ans=B[0]
if N==2:
    ans+=B[0]
else:
    for i in range(N-2):
        ans+=min(B[i],B[i+1])
    ans+=B[N-2]
print(ans)
