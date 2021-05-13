import bisect

n,k = map(int,input().split())
x = list(map(int,input().split()))

x.sort()

if x[-1] <= 0:
  print(abs(x[n-k]))
  exit()
elif x[0] >= 0:
  print(x[k-1])
  exit()

ans = []
if 0 not in x:
  x = [-10**10]*(10**6) + x + [10**10]*(10**6)
  ind = bisect.bisect_left(x,0)
  ans.append(abs(x[ind-k]))
  ans.append(x[ind+k-1])

  for i in range(ind-k+1,ind+k-1):
    a = 2*abs(x[i])+x[i+k-1]
    b = abs(x[i])+2*x[i+k-1]
    ans.append(min(a,b))
    
  print(min(ans))
  
else:
  x = [-10**10]*(10**6) + x + [10**10]*(10**6)
  ind = bisect.bisect_left(x,0)
  ans.append(abs(x[ind-k+1]))
  ans.append(x[ind+k-1])
  
  for i in range(ind-k+2,ind+k-1):
    a = 2*abs(x[i])+x[i+k-1]
    b = abs(x[i])+2*x[i+k-1]
    ans.append(min(a,b))
    
  print(min(ans))