import sys

n=int(input())
c=input()
black=c.count("#")
white=c.count(".")

if black==n:
  print(0)
  sys.exit()

b=0
w=0
now=0
ans=float('inf')

for i in range(n):
  if c[i]=="#":
    b+=1
  w=(i+1)-b

  now=b+(white-w)
  ans=min(ans,now)
  
print(min(ans,white))