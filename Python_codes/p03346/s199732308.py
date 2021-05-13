n = int(input())
pn = [0 for _ in  range(n)]
for i in range(n):
  p = int(input())
  pn[p-1] = i + 1

k = 1
tmpk = 1
for i in range(1, n):
  if pn[i-1] < pn[i]:
    tmpk += 1
  else:
    k = k if k > tmpk else tmpk
    tmpk = 1

k = k if k > tmpk else tmpk
print(n - k)
