n,a,b = map(int, input().split())
ans = 0
for i in range(n):
  s = str(i+1)
  tmp = 0
  for j in s:
    tmp += int(j)
  ans += i+1 if a <= tmp <= b else 0
print(ans)