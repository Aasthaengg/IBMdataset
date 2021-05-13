import io
import math

I=lambda:map(int,input().split())

h,w,d=I()

H={}

W={}

for i in range(1,h+1):
  for j,k in enumerate(I(),1):
    H[k],W[k]=i,j
    
x=1+h*w
s=[0 for _ in [0]*x]

for i in range(d+1,x):
  s[i]=s[i-d]+abs(H[i]-H[i-d])+abs(W[i]-W[i-d])

for _ in [0]*int(input()):
  a,b=I()
  print(s[b]-s[a])