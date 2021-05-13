n=int(input())
d,x=map(int,input().split())
for i in range(n):
  a=int(input())
  temp=1
  x=x+1
  while a*temp+1<=d:
    x=x+1
    temp=temp+1
print(x)
