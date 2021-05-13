a=int(input())
b=int(input())
c=int(input())
x=int(input())
ctr=0

def cal(p,q,r):
  s=500*p+100*q+50*r
  return s

for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      d=cal(i,j,k)
      if(d==x):
        ctr+=1

print(ctr)