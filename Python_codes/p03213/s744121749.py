def factorize(n):
    retlist = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            while temp%i==0:
                temp //= i
                retlist.append(i)
 
    if temp!=1:
        retlist.append(temp)
 
    if retlist==[]:
        retlist.append(n)
 
    return retlist
 
n=int(input())
a=[]
for i in range(1,n+1):
    a+=factorize(i)

from collections import Counter
c=Counter(a)
c=c.most_common()
c3=0
c5=0
c15=0
c25=0
c75=0
for k,v in c:
  if 2<=v<4:c3+=1
  elif 4<=v<14:c5+=1
  elif 14<=v<24:c15+=1
  elif 24<=v<74:c25+=1
  elif 74<=v:c75+=1
c3=c3+c5+c15+c25+c75
c5=c5+c15+c25+c75
c15=c15+c25+c75
c25=c25+c75
ans=0
ans+=(c5*(c5-1)//2)*(c3-2)
ans+=c15*(c5-1)
ans+=c25*(c3-1)
ans+=c75
print(ans)