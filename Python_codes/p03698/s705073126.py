import collections
S=collections.Counter(x for x in input())

for k,v in S.items():
  if v!=1:
    print('no')
    break
else:
  print('yes')