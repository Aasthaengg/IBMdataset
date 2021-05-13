N=int(input())
p=[int(input()) for i in range(N)]

p.sort()
ans=0
for j in range(N):
    if j==N-1:
        p[j]=p[j]//2
    ans+=p[j]
print(ans)
