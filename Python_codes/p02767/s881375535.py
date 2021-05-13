n = int(input())
X = list(map(int, input().split()))

ans = 10 ** 19
for i in range(101):
  ans = min(ans, sum((x - i) ** 2 for x in X))
  
print(ans)