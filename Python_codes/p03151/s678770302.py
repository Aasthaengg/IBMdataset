n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if sum(b) > sum(a):
  print(-1)
  exit()
d = []
minus = 0
minussum = 0
for i in range(n):
  k = a[i] - b[i]
  if k < 0:
    minus += 1
    minussum += k
  else:
    d.append(k)
d.sort(reverse=True)
for f in d:
  if minussum >= 0:
    print(minus)
    exit()
  minus += 1
  minussum += f
print(minus)