n = int(input())
a = list(map(int, input().split()))

total = sum(a)
ans = float("inf")
t = 0
for i in a:
  t += i
  total -= i
  ans = min(ans, abs(total-t))
print(ans)