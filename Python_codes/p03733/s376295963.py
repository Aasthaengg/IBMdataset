N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = T

for i in range(1,N):
  diff = t[i] - t[i-1]
  if diff < T:
    ans += diff
  else:
    ans += T

print(ans)  