N,L = map(int,input().split())

taste = [0]*N
for i in range(N):
  taste[i] = L + i

min_val = 10**3
min_idx = 0
for i in range(N):
  if min_val > abs(taste[i]):
    min_val = abs(taste[i])
    min_idx = i

ans = sum(taste)-taste[min_idx]
print(ans)