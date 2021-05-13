n, a, b = list(map(int, input().split()))
maxab = min(a, b)
minab = (a+b)-n
if minab < 0:
  minab = 0
  
print(maxab, minab)