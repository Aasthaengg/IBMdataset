n=int(input())
p=[int(input()) for i in range(n)]
p.sort()
ans = 0
ans+=p[-1]//2
for i in range(0,n-1):
    ans+=p[i]
print(ans)