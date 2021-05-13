n=int(input())
a=list(map(int,input().split()))
m=1
for i in a:
  m*=i
f=0
m-=1
for i in a:
  f+=m%i  
print(f)