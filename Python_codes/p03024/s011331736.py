# coding: utf-8
# user: herp_sy

import math
import statistics

win = 0
lose = 0
s = input()
for i in range(len(s)):
  if s[i] == 'o':
    win = win + 1
  else:
    lose = lose + 1
if(win + (15 - len(s)) >= 8):
  print('YES')
else:
  print('NO')
