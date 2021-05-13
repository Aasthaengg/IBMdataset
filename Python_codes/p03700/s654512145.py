n,a,b = map(int,input().split())
lis = [int(input()) for i in range(n)]
more = a-b

def tansaku(x):
  cou = 0
  normal = b * x
  for hp in lis:
    r = hp -normal
    if r <= 0:continue
    cou += r // more
    
    if r % more != 0:
      cou += 1
  return cou <= x

left = 1
right = max(lis)
while right - left > 1:
  mid = (right + left)//2
  if tansaku(mid):
    right = mid
  else:
    left = mid
print(right)
