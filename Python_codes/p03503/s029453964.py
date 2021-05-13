n=int(input())
f=[list(map(int,input().split())) for _ in range(n)]
p=[list(map(int,input().split())) for _ in range(n)]
ans=-10**10
for status in range(1,2**10):
    c=[0]*n
    cur=0
    for t in range(10):
        for i in range(n):
            if (status>>t)&1==1 and f[i][t]==1:
                c[i]+=1
    
    for i in range(n):
        cur+=p[i][c[i]]
    
    ans=max(ans,cur)

print(ans)
