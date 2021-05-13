from collections import Counter
n = int(input())
x = list(map(int,input().strip().split()))

rate = []
over = 0
for i in range(n):
  if x[i]//400 >=8:
    over += 1
  else:
    rate.append(x[i]//400)
elem = len(set(rate))

_min = elem
_max = elem +over
if elem  == 0:
  _min = 1
#if elem + over >=8:
#  _max = 8 

print(str(_min),str(_max))