n=int(input())
ans=0
for i in range(n):
    a,b=map(int, input().split())
    ans+=abs(a-b)+1
print(ans)