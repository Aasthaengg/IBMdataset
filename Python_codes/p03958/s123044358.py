k, t = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
double_cnt = 0
total = 0
for i in range(t):
  b = a[i] - double_cnt
  c = total - (double_cnt + 1) + 2
  double_cnt = max(0, b-c)
  total += a[i]
print(double_cnt)
