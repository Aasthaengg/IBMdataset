N,K = map(int,input().split())

if K == 0:
  print(N**2)
  exit()

ans = 0
for b in range(1,N+1):
  if b <= K: continue
  else: ans += N//b*(b-K) + max(0,(N-(N//b)*b)-K+1)

print(ans)