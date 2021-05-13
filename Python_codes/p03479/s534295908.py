from math import *

def solve(x,y,ans=1):
  if x*2 > y:
    return ans
  else:
    return solve(x*2,y,ans+1)
  
X,Y = map(int,input().split())
print(solve(X,Y))