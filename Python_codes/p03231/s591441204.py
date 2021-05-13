n,m=map(int,input().split())
s=list(input())
t=list(input())
import fractions
x=n*m//fractions.gcd(n,m)
s_lis=[i*x//n+1 for i in range(n)]
t_lis=[i*x//m+1 for i in range(m)]
import bisect
for i in range(n):
    ind=bisect.bisect_left(t_lis,s_lis[i])
    if ind==m:
        continue
    if t_lis[ind]==s_lis[i]:
        if s[i]!=t[ind]:
            print(-1)
            exit()

print(x)
