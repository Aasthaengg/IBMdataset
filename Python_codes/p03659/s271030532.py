n=int(input())

a = list(map(int,input().strip().split()))

su = a[0]
if n == 2:
  ar = a[1]
else:
  ar = sum(a[1:n])
dif = su-ar
mi = abs(dif)
for i in range(1,n-1):
  dif = dif+2*a[i]
  abs_dif = abs(dif)
  if mi > abs_dif:
    mi = abs_dif
print(mi)