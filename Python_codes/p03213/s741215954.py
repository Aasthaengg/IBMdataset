from collections import*
def cont(n):
  res=0
  n-=1
  for i in c:
    if i>=n:res+=1
  return res
def fact_p(n):
  m=n
  i=2
  a=[]
  while n>1:
    if i>m**.5:
      a+=[n]
      break
    if n%i==0:
      n//=i
      a+=[i]
    else:i+=1  
  return a
n=int(input())
a=[]
for i in range(1,n+1):
  a+=fact_p(i)
c=list(Counter(a).values())
print(cont(75)+cont(25)*(cont(3)-1)+cont(15)*(cont(5)-1)+cont(5)*(cont(5)-1)*(cont(3)-2)//2)