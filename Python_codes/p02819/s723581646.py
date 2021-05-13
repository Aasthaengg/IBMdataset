from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


class Eratos:
  def __init__(self, n):
    import math

    self.all = []
    self.is_prime = [True]*(n+1)
    self.is_prime[0] = False
    self.is_prime[1] = False

    for i in range(2, int(math.sqrt(n))+1):
      if self.is_prime[i]:
        self.all.append(i)
        j = i + i
        while j <= n:
          self.is_prime[j] = False
          j += i


def main():
  X = int(input())

  e = Eratos(X)

  # print(len(e.all))
  for x in range(X, 2*X+1):
    for prime in e.all:
      if x % prime == 0:
        break
    else:
      print(x)
      return


if(__name__ == '__main__'):
  main()
