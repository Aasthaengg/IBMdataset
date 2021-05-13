from itertools import product

n,m = map(int,input().split())
x=[0]*n
y=[0]*n
z=[0]*n

for i in range(n):
  x[i],y[i],z[i] = map(int,input().split())
  
sign = product([1,-1],repeat=3)
ans = 0
for s in sign:
  tmp = [0]*n
  for i in range(n):
    tmp[i] = s[0]*x[i] + s[1]*y[i] + s[2]*z[i]
  tmp = sorted(tmp,reverse=True)  
  tmp = sum(tmp[:m])
  ans = max(ans,tmp)
  
print(ans)  