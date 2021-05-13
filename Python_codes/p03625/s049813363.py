from collections import Counter
N = int(input())
A = list(map(int, input().split()))
c = Counter(A)
l = sorted(filter(lambda x:x[1] > 1,c.items()),reverse=True)

if len(l) == 0:
  print(0)
else:
  if l[0][1] >= 4:
    print(l[0][0]**2)
  else:
    print(l[0][0]*l[1][0])