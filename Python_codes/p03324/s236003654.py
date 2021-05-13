d,n = map(int,input().split())
ans = n
if d != 0:
    ans *= 100**d

if n == 100:
    ans += 100**d

print(ans)