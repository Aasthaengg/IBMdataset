a,b,c,k = list(map(int,input().split()))
ans = 0

if a <= k:
  ans += a
  k -= a
else:
  ans += k
  k = 0

if b <= k:
  k -= b
else:
  k = 0

ans -=k

print(ans)