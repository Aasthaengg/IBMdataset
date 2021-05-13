import collections
A=collections.Counter(map(int,input().split()))
for  k,v in A.items():
  if v==1:
    print(k)