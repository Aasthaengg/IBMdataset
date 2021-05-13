n,d=map(int,input().split())
p=0
while n>0:
  n-=(d*2+1)
  p+=1
print(str(p))