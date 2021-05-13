N,A,B = map(int,input().split())
H = [int(input()) for _ in range(N)]

def calc(x):
  bomb = 0
  for h in H:
    if h > B*x:
      bomb += ((h-B*x)-1)//(A-B) +1
  return (x >= bomb)

def check(a,b):
  mid = (a+b)//2
  if a == mid:
    return b
  if calc(mid):
    return check(a,mid)
  else:
    return check(mid,b)

print(check(0,10**9))