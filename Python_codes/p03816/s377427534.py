from math import ceil

n=int(input())
a=list(map(int,input().split()))


cnt=[0]*100010
lst=[]

for i in a:
  cnt[i]+=1

for i in cnt:
  if i<=1:
    continue
  
  else:
    x=i-1
    lst.append(x)

print(n-ceil(sum(lst)/2)*2)