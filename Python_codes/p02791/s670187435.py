n=int(input())
p=list(map(int,input().split()))
t=0
ans=0
for i in range(n):
    if t>=p[i] or t==0:
        ans+=1
        t=p[i]
print(ans)