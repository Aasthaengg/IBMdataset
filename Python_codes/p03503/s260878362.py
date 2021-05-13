import itertools
n=int(input())
f=[tuple(map(int,input().split())) for _ in range(n)]
p=[tuple(map(int,input().split())) for _ in range(n)]
ll=list(itertools.product(range(2),repeat=10))[1:]
ans=-10**10
for l in ll:
    t=0
    for i in range(n):
        c=0
        for j in range(10):
            if l[j]==1:
                if f[i][j]==l[j]:
                    c+=1
        t+=p[i][c]
    ans=max(ans,t)
print(ans)