n,a,b = list(map(int, input().split()))

if a < b:
  max = a
else:
  max = b

min = (a + b) - n
if min < 0:
  min = 0
 
print(max, min)