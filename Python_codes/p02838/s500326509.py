n = int(input())
A = list(map(int,input().split()))
a = [format(i,'b') for i in A]
ans = 0
mod = 10**9+7
for i in range(60):
  cnt = 0
  for v in a:
    if len(v)<i+1:
      continue
    if v[-1-i]=='1':
      cnt += 1
  cnt = cnt*(n-cnt)%mod
  ans += cnt*(2**i)%mod
print(ans%mod)