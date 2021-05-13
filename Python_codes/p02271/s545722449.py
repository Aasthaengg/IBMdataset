# -*- coding: utf-8 -*-
from sys import stdin

n = int(stdin.readline().rstrip())
A = list(map(int,stdin.readline().split()))
q = stdin.readline().rstrip()
M = list(map(int, stdin.readline().split()))

sum_results = set()

for i in range(2 ** n):
  sum_tmp = 0
  for j in range(n):
    # print("pattern i:{} j:{} i>>j{}".format(i,j,i>>j))

    if ((i >> j) & 1):  #順に右にシフトさせ最下位bitのチェックを行う
      sum_tmp += A[j]
  else:
    sum_results.add(sum_tmp)

for m in M:
  if m in sum_results:
    print("yes")
  else:
    print("no")

