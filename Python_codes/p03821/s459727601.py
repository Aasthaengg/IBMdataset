n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
ans=0
for b,a in l[::-1]:
    d=(a-(b+ans)%a)%a
    ans+=d
print(ans)