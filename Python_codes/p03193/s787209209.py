n,h,w = (int(i) for i in input().split())
a = []
for i in range(n):
  tmp = list(int(i) for i in input().split())
  a.append(tmp)
ct = 0
for i in range(n):
  if a[i][0] >= h and a[i][1] >=w: ct += 1
print(ct)