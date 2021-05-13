n,m = map(int,input().split())
import math 

if n>=2 and m>=2:
  ans = math.factorial(n)/math.factorial(n-2)/math.factorial(2) + math.factorial(m)/math.factorial(m-2)/math.factorial(2)

elif n<2 and m>=2 :
  ans =  math.factorial(m)/math.factorial(m-2)/math.factorial(2)

elif m<2 and n>=2:
  ans = math.factorial(n)/math.factorial(n-2)/math.factorial(2)

else:
  ans = 0

print(int(ans))