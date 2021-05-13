n = int(input())
a = list(map(int,input().split()))
a.sort()
ret = 0
method = []

ret = a[0]
d = 2
while d < n and a[-d] > 0:
  method.append((ret, a[-d]))
  ret -= a[-d]
  d += 1
method.append((a[-1], ret))
ret = a[-1] - ret
for i in range(1, n-d+1):
  method.append((ret, a[i]))
  ret -= a[i]

print(ret)
for t in method: print(*t)
