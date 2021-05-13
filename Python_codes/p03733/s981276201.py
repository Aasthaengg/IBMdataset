N,T = map(int,input().split())
t = list(map(int,input().split()))
X = 0
for i in range(N):
  if i==0: #1st 
    end = T #お湯が止まる時間
  
  elif t[i]>end: 
    X+=T
  elif t[i]<=end:
    X+=t[i]-t[i-1]
    
  end = t[i]+T

X+=T #last
print(X)