n,k = map(int, input().split())

ans = 0
for i in range(1,n+1):
  t = 0
  while i < k:
    i*=2
    t += 1
  ans += 0.5**t/n
print(ans)