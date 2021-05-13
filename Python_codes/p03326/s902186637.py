n,m=map(int,input().split())
x=[0]*n
y=[0]*n
z=[0]*n
for i in range(n):
  x[i],y[i],z[i]=map(int,input().split())
ans=0
for j in range(2):
  for k in range(2):
    for l in range(2):
      A=[]
      for i in range(n):
        A.append(x[i]*(-1)**j+y[i]*(-1)**k+z[i]*(-1)**l)
      A.sort(reverse=True)
      a=0
      for i in range(m):
        a=a+A[i]
      if a>ans:
        ans=a
print(ans)