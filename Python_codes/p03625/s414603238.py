import collections

n=int(input())
arr=list(map(int,input().split()))
cnt=collections.Counter(arr)
keys=cnt.keys()
keys=sorted(keys,reverse=True)
a=0
b=0
for key in keys:
  if b!=0:
    break
  if a==0:
    if cnt[key]>=2:
      a=key
      if cnt[key]>=4:
        b=key
  else:
    if cnt[key]>=2:
      b=key
print(a*b)