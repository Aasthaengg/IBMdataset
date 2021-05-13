n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))

s=abs(a-(t-h[0]*0.006))
x=1

for i in range(n):
  z=t-h[i]*0.006
  if s > abs(a-z):
    s=abs(a-z)
    x=i+1
   
print(x)