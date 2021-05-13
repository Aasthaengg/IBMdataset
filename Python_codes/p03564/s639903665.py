N=int(input())
K=int(input())

ans=float("inf")
for i in range(2**N):
    val=1
    for j in range(N):
        if i%2==0:
            val*=2
            i//=2
        else:
            val+=K
            i//=2
    ans=min(ans,val)
print(ans)