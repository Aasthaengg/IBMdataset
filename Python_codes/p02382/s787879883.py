n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

a = [abs(x[i] - y[i]) for i in range(n)]

for p in range(1, 4):
  ans = 0
  for d in a:
    ans += d ** p
  print('{:.10f}'.format(ans ** (1/p)))
print('{:.10f}'.format(max(a)))

