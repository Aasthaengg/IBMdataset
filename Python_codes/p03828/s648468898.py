from collections import Counter
def p_fact(n):
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
a=[]
for i in range(1,int(input())+1):
  a+=p_fact(i)
ans=1
mod=10**9+7
for i in list(Counter(a).values()):
  ans*=(i+1)
  ans%=mod
print(ans)