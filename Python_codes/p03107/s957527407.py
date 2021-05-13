import collections
n=str(input())
lst=list(collections.Counter(n).most_common())
if len(lst)==1:
  print(0)
else:
  print(lst[1][1]*2)