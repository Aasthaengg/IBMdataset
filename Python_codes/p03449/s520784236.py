n=int(input())
a=[list(map(int,input().split())) for i in range(2)]
ans=0
num=0
for i in range(n):
    num=(sum(a[0][:i+1])+sum(a[1][i:]))
    if num>ans:
        ans=num
print(ans)