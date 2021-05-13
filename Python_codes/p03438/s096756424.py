import math
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) > sum(b):
  print ('No')
  exit()
elif sum(a) == sum(b):
  for i in range(n):
    if a[i] != b[i]:
      print ('No')
      exit()
  print ('Yes')
  exit()

s = sum(b)-sum(a)
c = 0
for i in range(n):
  if a[i] < b[i]:
    c += math.ceil((b[i]-a[i])/2)
if c > s:
  print ('No')
else:
  print ('Yes')