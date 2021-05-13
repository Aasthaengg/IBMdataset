n = int(input())
q = list(map(int, input().split()))

mod = 10**9+7
ans = 1
hat = [0, 0, 0]

for i in range(n):
  count = hat.count(q[i])
  ans *= count
  ans %= mod
  if ans == 0:
    break
  for j in range(3):
    if hat[j] == q[i]:
      hat[j] += 1
      break
      
print(ans)