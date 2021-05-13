from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


def check(min_, max_, x):
  if max_ <= x:
    # return 10**max(0, len(str(min_))-2)
    return int((max_ - min_)/10) + 1
  elif min_ <= x:
    # ret = max(1, int(str(x)[1:-1]) if len(str(x)) > 2 else 1)
    # if int(str(min_)[-1]) <= int(str(x)[-1]):
    #   ret += 1
    # return ret
    return int((x - min_)/10) + 1
  else:
    return 0


def main():
  N = int(input())

  if len(str(N)) == 1:
    print(N)
    return
  sum_ = 0
  for l in range(1, 10):
    for r in range(l, 10):
      temp = sum_
      min_ = int(str(l) + '0'*(len(str(N))-2) + str(r))
      max_ = int(str(l) + '9'*(len(str(N))-2) + str(r))
      A = check(min_, max_, N)
      # max_ = int(str(l) + '9'*(len(str(N))-3) + str(r))
      for gap in range(len(str(N))-2):
        A += (10**gap)

      min_ = int(str(r) + '0'*(len(str(N))-2) + str(l))
      max_ = int(str(r) + '9'*(len(str(N))-2) + str(l))
      B = check(min_, max_, N)
      for gap in range(len(str(N))-2):
        B += (10**gap)

      if l == r:
        A += 1
        B += 1
        sum_ += A*B
      else:
        sum_ += 2*A*B
      # print(l, r, sum_ - temp)

  print(sum_)


if(__name__ == '__main__'):
  main()
