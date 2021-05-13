A,B,C,K=map(int,input().split())
ans=0
if K<A:
    ans=K
elif K<A+B:
    ans=K
else:
    ans=A-(K-(A+B))
print(ans)