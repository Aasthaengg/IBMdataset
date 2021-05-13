n,m=map(int,input().split())
a=list(map(int,input().split()))
da=[9,8,7,6,5,4,3,2,1]
db=[6,7,3,6,5,4,5,5,2]
ka=set(())
d={}
for i in range(9):
  if  da[i] in a and db[i] not in ka:
    d[da[i]]=db[i]
    ka.add(db[i])
dr={v:k for k,v in d.items()}
a=[d.keys()]
a.sort(reverse=True)

dp=[0]*(n+1)
dp[0]=''
import sys
sys.setrecursionlimit(10**7)
def maxret(d1,d2):
  if len(d1)>len(d2):return d1
  if len(d1)<len(d2):return d2
  if d1>d2:return d1
  if d1<d2:return d2
def func(k):
  if k==0:return ''
  if dp[k]!=0:return dp[k]
  ret=''
  for x in d:
    if k-d[x]<0:continue
    tmp=func(k-d[x])
    tmp+=str(x)
    if tmp[0]=='-':continue
    t=maxret(ret,tmp)
    ret=t
  if ret=='':
    dp[k]='-'
  else:
    dp[k]=ret
  return dp[k]
ddd=func(n)
print(ddd)
