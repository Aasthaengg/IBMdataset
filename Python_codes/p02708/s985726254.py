n,k = map(int,input().split())

mod = 10**9 + 7
# k個選ぶときからn-1個選ぶとき
ans = 0
for i in range(k, n+1):
  min = 1/2 * (i-1) * i
  max = 1/2 * (n-i+1+n) * (n-(n-i+1)+1)
  ans += (max - min + 1) % mod
print(int(ans + 1)% mod)

