n,c=map(int,input().split())
a=1
c=c-1
for i in range(n-1):
  a=a*c
print(a*(c+1))