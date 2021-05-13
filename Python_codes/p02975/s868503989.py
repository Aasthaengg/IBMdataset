from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)

for i in a:
  d[i] += 1

a.sort()
if max(a) == 0 and min(a) == 0:
  print ('Yes')
  exit()
b = set(a)
if len(b) == 3:
  c = 0
  for i in b:
    c ^= i
  if c == 0:
    flg = 0
    for i in d:
      if d[i] != n/3:
        flg = 1
    if flg == 1:
      print ('No')
    else:
      print ('Yes')
  else:
    print ('No')
  exit()
else:
  if min(a) == 0 and d[min(a)] ==n/3 and d[max(a)] == (2*n)/3:
    print('Yes')
  else:
    print ('No')
  exit()
print ('No')

