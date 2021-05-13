n = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for i in range(n):
  t = V[i] -C[i]
  if(t >= 0):
    ans += t
print(ans)