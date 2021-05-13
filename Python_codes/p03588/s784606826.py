n=int(input())
m=0
x=0
for i in range(n):
  a,b=map(int,input().split())
  if a>m:
    m=a
    x=a+b
print(x)