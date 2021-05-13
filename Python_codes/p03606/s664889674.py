n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]

ans=n
for i in range(n):
    ans+=(l[i][1]-l[i][0])
print(ans)