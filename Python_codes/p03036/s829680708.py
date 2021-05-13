r,d,x = map(int, input().split())

a = [0]*10
a[0] = r*x-d
print(a[0])
for i in range(1, 10):
  s = r*a[i-1] -d
  a[i] = s
  print(s)