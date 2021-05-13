n=int(input())
ans=n
for i in range(n):
    a,b=map(int,input().split())
    ans+=(b-a)

print(ans)