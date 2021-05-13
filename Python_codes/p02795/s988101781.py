h=int(input())
w=int(input())
n=int(input())
c1=0
c2=0
t=0
while t<n:
  if h-c2<=w-c1:
    t+=w-c1
    c2+=1
  else:
    t+=h-c2
    c1+=1
print(c1+c2)