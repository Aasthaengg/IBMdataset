def solve(a,b):
  def needTaps(a,b,holes=1,res=0):
    if holes >= b:
      return res
    else:
      return needTaps(a,b,holes+a-1,res+1)
    
  return needTaps(a,b)

a,b=map(int,input().split())
print(solve(a,b))
