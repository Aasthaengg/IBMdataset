n,a,b = map(int, input().split())
ans = 0
for i in range(n):
  s = i+1
  tmp = 0
  while s > 0:
    tmp += s%10
    s = s//10
  ans += i+1 if a <= tmp <= b else 0
print(ans)