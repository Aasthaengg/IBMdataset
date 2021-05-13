N=int(input())
TA=[list(map(int, input().split())) for i in range(N)]

nums=TA[0]

def f(points, rate):
  if points[0]%rate[0]>0:
    a=1
  else:
    a=0
  if points[1]%rate[1]>0:
    b=1
  else:
    b=0
    
  tmp=max(points[0]//rate[0]+a, points[1]//rate[1]+b)
  return [rate[0]*tmp, rate[1]*tmp]

for i in range(1, N):
  nums=f(nums, TA[i])
  
print(sum(nums))