n,a,b = map(int,input().split())

if a+b-n > 0:
  result = a +b-n
else:
  result = 0

print(min(a,b),result)