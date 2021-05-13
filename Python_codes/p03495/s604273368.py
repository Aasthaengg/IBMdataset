import sys
from collections import Counter
n,k = map(int,input().split())
a = list(map(int,input().split()))
counter = Counter(a)
cnt = 0

c_value= list(counter.values())
nl = len(c_value)
if nl <= k:
  print(0)
  sys.exit()
  
c_value.sort()
#print(c_value)
do_num = nl - k
for i in range(do_num):
  cnt += c_value[i]
print(cnt)