n = int(input())
alst = list(map(int, input().split()))
total = sum(alst)
x = alst[0]
ans = abs(total - 2 * x)
for a in alst[1:-1]:
  x += a
  ans = min(abs(total - 2 * x), ans)
print(ans)