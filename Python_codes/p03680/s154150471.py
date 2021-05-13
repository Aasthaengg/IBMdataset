from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = [int(input())-1 for _ in range(N)]

  next_ = A[0]
  cnt = 1
  lighten = set([0])
  while True:
    if next_ == 1:
      print(cnt)
      return
    if next_ in lighten:
      break
    lighten.add(next_)
    next_ = A[next_]
    cnt += 1

  print(-1)


if(__name__ == '__main__'):
  main()
