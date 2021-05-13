import sys 
sys.setrecursionlimit(10**6)
def dp(n,cache,height):
  if n<0:
    return float('inf')
  elif n==0:
    return 0
  elif n==1:
    return abs(height[1]-height[0])
  elif n in cache :
    return cache[n]
  else:
    cache[n]= min(dp(n-1,cache,height)+abs(height[n]-height[n-1]),dp(n-2,cache,height)+abs(height[n]-height[n-2]))
    return cache[n]
n=int(input())
h=list(map(int,input().split()))
print(dp(n-1,dict(),h))
