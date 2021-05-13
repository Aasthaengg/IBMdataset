from collections import Counter
n = int(input())
lst = list(map(int, input().split()))
odd = Counter(lst[::2])
even = Counter(lst[1::2])
#print(odd, even)
omax = odd.most_common()[0]
emax = even.most_common()[0]
if len(odd) >= 2:
  osec = odd.most_common()[1]
if len(even) >= 2:
  esec = even.most_common()[1]
#print(omax, emax)

if omax[0] == emax[0]:
  if len(even) == 1 and len(odd) == 1:
    print(n // 2)
  elif len(even) == 1:
    print(n - emax[1] - osec[1])
  elif len(odd) == 1:
    print(n - omax[1] - esec[1])
  else:
    print(min(n - emax[1] - osec[1], n - omax[1] - esec[1]))
else:
  print(n - omax[1] - emax[1])