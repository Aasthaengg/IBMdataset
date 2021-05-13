n = int(input())
a = list(map(int, input().split()))
sl = []
for i in range(n):
  s = a[i] - 1
  sl.append(s)
print(sum(sl))