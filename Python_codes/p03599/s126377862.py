#!/usr/bin/python3
# -*- coding:utf-8 -*-

import numpy
from queue import deque

def main():
  l = list(map(int, input().split()))
  w1, w2, s1, s2, spwr, mm = l
  w1, w2 = 100*w1, 100*w2
  flags = numpy.zeros((mm+1, mm+1))
  dq = deque([(w1, 0)])
  max_conc = -1.0
  ans = (0, 0)
  while dq:
    w, s = dq.pop()
    flags[w, s] = 1
    if w != 0 and s <= spwr * w // 100:
      conc = s / (w + s)
      if max_conc < conc:
        max_conc = conc
        ans = (w+s, s)
    for sx in [s1, s2]:
      if w + s+sx <= mm and flags[w, s+sx] == 0:
        flags[w, s+sx] = 1
        dq.append((w, s+sx))
    for wx in [w1, w2]:
      if w+wx + s <= mm and flags[w+wx, s] == 0:
        flags[w+wx, s] = 1
        dq.append((w+wx, s))
  print(*ans)
  
if __name__=='__main__':
  main()

