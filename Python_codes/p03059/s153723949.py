a,b,t = map(int,input().split())
ans = 0
while t >= a:
    ans += b
    t -= a

print(ans)