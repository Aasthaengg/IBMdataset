n = int(input())
d = list(map(lambda x: int(x), input().split(" ")))
ans = 0
for i in range(n - 1):
  ans += d[i] * sum(d[i + 1:])
  
print(ans)