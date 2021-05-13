from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
cnt=defaultdict(int)
for i in range(n):
  cnt[a[i]]+=1
tmp=[]
for key in cnt.keys():
  if cnt[key]>=2:
    tmp.append(key)
    if cnt[key]>=4:
      tmp.append(key)
tmp=sorted(tmp,reverse=True)
if len(tmp)<=1:
  print(0)
else:
  print(tmp[0]*tmp[1])