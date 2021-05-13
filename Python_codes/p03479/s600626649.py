X,Y = map(int,input().split())

def solve(now,y,ans=1):
  if now*2 > y:
    return ans
  else:
    return solve(now*2,y,ans+1)
  
print(solve(X,Y))