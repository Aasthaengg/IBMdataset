N = int(input())
l = len(str(N))
d = [0,9,0,900,0,90000]
res = 0
for i in range(l):
  res += d[i]
if l == 1:
  res += N
if l == 3:
  res += (N - 99)
if l == 5:
  res += (N - 9999)
print(res)