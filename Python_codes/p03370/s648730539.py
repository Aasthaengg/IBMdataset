n,x=map(int,input().split())
m=[0]*n
for i in range(0,n):
  m[i]=int(input())
  x=x-m[i]
print(int(x/min(m))+n)