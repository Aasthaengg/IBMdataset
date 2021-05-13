n,t = map(int,input().split())
t_li = list(map(int,input().split()))
ans = 0
for i in range(n-1):
    dum = t_li[i+1]-t_li[i]
    if dum < t:
        ans += dum
    else:
        ans += t
print(ans+t)