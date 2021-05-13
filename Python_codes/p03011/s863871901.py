a = list(map(int, input().split()))

b = a[0] + a[1]

if b > a[1] + a[2]:
  b = a[1] + a[2]

if b > a[2] + a[0]:
  b = a[2] + a[0]
  
print(b)