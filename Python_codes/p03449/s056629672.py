n=int(input())
a=[list(map(int, input().split())) for _ in range(2)]

ans=0
s=sum(a[0]+a[1])
for i in range(n):
    tmp_ans=s-(sum(a[1][:i])+sum(a[0][i+1:]))
    ans=max(ans,tmp_ans)
print(ans)
