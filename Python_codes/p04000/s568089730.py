h,w,n = [int(_) for _ in input().split(" ")]
d = {}
for _ in range(n):
  a, b = [int(_) for _ in input().split(" ")]
  for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
      k = (a+i,b+j)
      if k in d:
        d[k] += 1
      else:
        d[k] = 1

ans = {i:0 for i in range(1,10)}
s = 0
for k, v in d.items():
  if 1 < k[0] < h and 1 < k[1] < w:
    ans[v] += 1
    s += 1
ans[0] = (w-2) * (h-2) - s

for _ in range(10):
  print(ans[_])