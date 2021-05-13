import math
import sys
n = int(input())
t = [int(input()) for _ in range(n)]
if n == 1:
  print(t[0])
  sys.exit()
elif n == 2:
  print((t[0]*t[1])//(math.gcd(t[0],t[1])))
  sys.exit()
t.sort()
ans = (t[0]*t[1])//math.gcd(t[0],t[1])
for i in range(2,n-1):
    #print((ans*t[i])//math.gcd(ans,t[i]))
    ans =((t[i]*ans)//math.gcd(t[i],ans))
print((ans*t[-1])//math.gcd(ans,t[-1]))
