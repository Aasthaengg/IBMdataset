n,t = map(int, input().split())
a = list(map(int, input().split()))
tmp = t
for i in range(n - 1):
  if a[i] + t > a[i+1]:
    tmp = tmp + a[i+1] - a[i]
  else:
    tmp = tmp + t
print(tmp)