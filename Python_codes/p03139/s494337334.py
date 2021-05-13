n,a,b = map(int, input().split())
maxint = 0
minInt = 0
if a <= b:
  maxInt = a
  minInt = a - (n-b)
else:
  maxInt = b
  minInt = b - (n-a)

if a +b < n :
    minInt = 0
print(maxInt, minInt)