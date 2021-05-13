N, K = list(map(int,input().split()))
xlist = list(map(int,input().split()))

def f(min1,max1):
  if min1>=0 and max1>=0:
    return abs(max1)
  elif min1<=0 and max1 <=0:
    return abs(min1)
  else:
    return min([-2*min1 + max1,-min1 + 2*max1])

ans = 2*10**9
for i in range(N-K+1):
  min1 = xlist[i]
  max1 = xlist[i+K-1]
  dist =f (min1,max1) 
  if dist < ans :
    ans = dist

print(ans)
