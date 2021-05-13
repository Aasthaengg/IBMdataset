# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline
from collections import deque
sa = deque(list(str(input()).replace('\n', '')))
sb = deque(list(str(input()).replace('\n', '')))
sc = deque(list(str(input()).replace('\n', '')))
di = {'a':sa, 'b':sb, 'c':sc}
turn = 'a'
while True:
  turn = di[turn].popleft()
  # print(turn)
  if len(di[turn])==0:
    print(turn.upper())
    break