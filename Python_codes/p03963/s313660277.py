N, K = map(int, input().split())
ans = 1

for n in range(N):
  if n == 0:
    ans *= K
  else:
    ans *= K-1
  
print(ans)