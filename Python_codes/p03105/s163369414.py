a, b, c = map(int, input().split())
ans = 0
for i in range(1, c+1):
  if a*i <= b:
    ans += 1
print(ans)