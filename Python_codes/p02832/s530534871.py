from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = list(map(int, input().split()))
  A = A

#  pre = A[0]
#  right = -1
#  left = 0
#  max_ = 0
#  for i in range(1, N):
#    if pre+1 == A[i]:
#      right = i
#    else:
#      max_ = max(max_, right-left)
#      left = i
#  max_ = max(max_, N-left)

  max_ = 0
  for i in range(N):
    if max_ + 1 == A[i]:
      max_ = A[i]

  print(N-max_ if max_ else -1)


if(__name__ == '__main__'):
  main()
