N = int(input())
K = int(input())
ans = 1

for i in range(1,N+1):
  if 2**(i-1) < K:
    ans = ans + 2**(i-1)
  else:
    ans = ans + K
print(ans)