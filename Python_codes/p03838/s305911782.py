x,y=[int(_) for _ in input().split()]

def a():
  if y<x:
    return 10000000000
  return y-x
def ba():
  if -x>y:
    return 10000000000
  return y+x+1

def ab():
  if x>-y:
    return 100000000000
  return -x-y+1
def bab():
  if x<y:
    return 10000000000
  return x-y+2
ans=min(a(),ba(),bab(),ab())
print(ans)