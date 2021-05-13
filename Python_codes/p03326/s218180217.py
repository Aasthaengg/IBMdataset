# データ読み込み

import sys
from collections import deque

def input_data(d=""):
  t = sys.stdin.read()
  if t:
    return t
  else:
    if d[0] == "\n":
      d = d[1:]
    if d[-1] == "\n":
      d = d[:-1]    
    return d

A,AA, *B  = map(int,input_data().split())

m = []

out = 0
t = [[] for i in range(8)]
for a,b,c  in zip(*[iter(B)] * 3):
  t[0].append(a+b+c)
  t[1].append(a+b-c)
  t[2].append(a-b+c)
  t[3].append(a-b-c)
  t[4].append(-a+b+c)
  t[5].append(-a+b-c)
  t[6].append(-a-b+c)
  t[7].append(-a-b-c)
for i in range(8):
  t[i].sort(reverse=True)
  if out < sum(t[i][:AA]):
    out = sum(t[i][:AA])
print(out)