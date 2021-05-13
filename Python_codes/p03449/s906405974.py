n=int(input())
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
ans=0
for i in range(n):
    B1=A1[:i+1]
    B2=A2[i:]
    ans=max(ans,sum(B1)+sum(B2))
print(ans)