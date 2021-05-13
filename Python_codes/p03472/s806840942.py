n,h = map(int,input().split())
a_list = []
b_list = []
use_b_list = []
for i in range(n):
  a,b = map(int,input().split())
  a_list.append(a)
  b_list.append(b)
use_a = max(a_list)
import math
for b in b_list:
  if b > use_a:
    use_b_list.append(b)
use_b_list.sort(reverse = True)    
count = 0
if sum(use_b_list) >= h:
  for i in range(len(use_b_list)):
    h -= use_b_list[i]
    count += 1
    if h <= 0:
      break
  print(count)
else:
  h -= sum(use_b_list)
  print(len(use_b_list) + int(math.ceil(h/max(a_list))))