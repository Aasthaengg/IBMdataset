n,m,d = map(int,input().split())
ans = (m-1) * (((n-d)*2)/(n**2))
if d == 0:
    ans /= 2
print(ans)
