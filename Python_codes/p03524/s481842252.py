from collections import defaultdict
s = input()

d = defaultdict(int)

for i in s:
  d[i] += 1

if len(s) == 1:
  print ('YES')
  exit()
if len(d) == 1:
  print ('NO')
  exit()
if len(d) == 2:
  if len(s) == 2:
    print ('YES')
    exit()
  else:
    print ('NO')
    exit()


a = list(d.values())
if max(a) - min(a) < 2:
  print ('YES')
else:
  print ('NO')
