from math import*
def fact_p(n):
  m=n
  i=2
  a=0
  while n>1:
    if i>m**.5:
      a=n
      break
    while n%i==0:
      n//=i
      a=i
    i+=1  
  return a
n=int(input())
x2=y1=ceil(n**.5+.5) if ceil(n**.5+.5)<=10**9 else 10**9
x1=fact_p(x2*y1-n)
y2=(x2*y1-n)//x1 if x1 else 0
print(0,0,x1,y1,x2,y2)