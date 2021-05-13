n = int(input())
a = list(map(int, input().split()))
mean = sum(a) / n
INF = 10**5
flg = INF
for i in range(n):
  if abs(mean - a[i]) < flg:
    idx = i
    flg = abs(mean - a[i])
print(idx)
