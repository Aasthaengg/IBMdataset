N = int(input())
ans = 0
tmp = 0
for _ in range(N):
  a, b = map(int, input().split())
  if a == b:
    tmp += 1
  else:
    tmp = 0
  ans = max(ans, tmp)

print("Yes" if ans >= 3 else "No")