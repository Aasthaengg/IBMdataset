K,T=map(int,input().split())
*A,=map(int,input().split())
ans=0
H=0--K//2
for a in A:
    if a>H:
        ans+=2*a-K-1
print(ans)