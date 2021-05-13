n,a,b = map(int, input().split())
if a+b > n:
  q = a+b-n
else :
  q = 0
print( str(min(a,b)) +" "+ str(q))