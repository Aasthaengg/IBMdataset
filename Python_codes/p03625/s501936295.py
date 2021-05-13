import collections 

n = int(input())
A = list( map(int, input().split()))

d = collections.Counter(A)

x = sorted([i for i in d.items() if i[1]>1])
if len(x)==0 :
  print(0)
elif x[-1][1] >3 :
  print(x[-1][0]**2)
elif len(x) == 1 :
  print(0)
else:
  print(x[-1][0]*x[-2][0])