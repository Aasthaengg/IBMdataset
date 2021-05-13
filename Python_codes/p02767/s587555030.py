n = int(input())
a = sorted(map(int, input().split()))
ans = 10000000000
for p in range(1,101):
  tmp = 0
  for j in a:
    tmp += (p-j)**2
  ans = min(tmp,ans)
print(ans)