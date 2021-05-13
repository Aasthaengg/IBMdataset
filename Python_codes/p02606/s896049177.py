a=input().split()
b = int(a[0])
c = int(a[1])
d = int(a[2])
e = int(c // d - b // d)

if b % d == 0:
  e = e+1

print(int(e))