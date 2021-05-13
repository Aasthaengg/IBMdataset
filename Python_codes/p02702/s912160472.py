from collections import deque
s  = input()[::-1]
lsts = [0] * 2019
kai = 1
cou = 0
st = 0
lsts[0] = 1
for i in s:
  st += int(i) * kai
  st %= 2019
  cou += lsts[st]
  lsts[st] += 1  
  kai = kai * 10 % 2019

print(cou)