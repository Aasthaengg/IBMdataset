n=int(input())
from collections import Counter as co
l=co(list(map(int,input().split()))).values()
ans=0
p=0

for i in l:
  if (i-1)%2==0:ans+=1
  else:p+=1
print(ans+p//2*2)