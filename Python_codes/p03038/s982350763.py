n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
from itertools import accumulate
from bisect import bisect_left
from collections import Counter
dic=Counter(a)
for i in range(m):
  b,c=list(map(int,input().split()))
  dic[c]=dic.get(c,0)+b

dic=sorted(dic.items(),key=lambda x:x[0],reverse=True)

ans=0
num=0
for i in dic:
  num=num+i[1]
  ans=ans+i[0]*i[1]
  if num>=n:
    r=i[0]
    break
 
print(ans-(num-n)*r)


  
