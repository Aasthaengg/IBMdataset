N = int(input())
x = list(map(int, input().split()))
import copy
a = copy.copy(x)
a.sort()
m = a[N//2-1]
for i in range(N):
  if x[i] <= m:
    print(a[N//2])
  else:
    print(m)