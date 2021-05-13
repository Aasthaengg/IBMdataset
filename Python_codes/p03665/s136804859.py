import collections
n, p = list(map(int, input().split()))
a = list(map(int, input().split()))
a2 = [ai%2 for ai in a]
a2 = collections.Counter(a2)

if p == 0:
  if a2[1] == 0:
    print(2 ** n)
  else:
    print(2 ** (n - 1))
    
else:
  if a2[1] == 0:
    print(0)
  else:
    print(2 ** (n-1))

