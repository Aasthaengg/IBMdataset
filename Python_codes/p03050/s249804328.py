import math
n = int(input())
s = 0
if math.sqrt(n) == int(math.sqrt(n)):
  lim = int(math.sqrt(n))
else:
  lim = int(math.sqrt(n))+1
for i in range(1,lim):
  x = n-i
  if x%i == 0 and x//i > i:
    s += x//i
print(s)
