from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  P = list(map(int, input().split()))

  min_ = float('inf')
  cnt = 0
  for i in range(N):
    if P[i] < min_:
      cnt += 1
      min_ = P[i]

  print(cnt)


if(__name__ == '__main__'):
  main()
