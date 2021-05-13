n,x = map(int, input().split())
l = list(map(int, input().split()))
d = 0
times = 1
for i in range(n):
  d += l[i]
  if d > x:
    break
  times += 1
print(times)