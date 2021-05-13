from collections import Counter
 
N = int(input())
d = Counter(map(int, input().split()))
 
sticks_len = []
for k, v in d.items():
  if v >= 2:
    sticks_len.append(k)
  if v >= 4:
    sticks_len.append(k)
    
sticks_len.sort()
 
if len(sticks_len) >= 2:
  print(sticks_len[-1] * sticks_len[-2])
else:
  print(0)
 
