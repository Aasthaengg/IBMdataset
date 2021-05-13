n=int(input())
x=0
while x*(x+1)//2<n:
  x+=1
for i in range(1,x+1):
  if not x*(x+1)//2-i==n:
    print(i)