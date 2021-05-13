X,Y = map(int,input().split())

def solve(now,y,ans=0):
  ans = 0
  while now <= y:
    ans += 1
    now *= 2
  return ans
  
print(solve(X,Y))