from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
import math
from sys import stdin
input = stdin.readline


def main():
  a, b, x = list(map(int, input().split()))

  # y = 2*(b-(x/a**2))/a
  # yd = 2*x/(a*b**2)
  # print(y, yd)
  if x > 0.5*a*a*b:
    print(math.degrees(math.atan( 2*(b-(x/a**2))/a )))
  else:
    print(90 - math.degrees(math.atan( (2*x/(a*b**2)) )))


if(__name__ == '__main__'):
  main()
