import math
from sys import stdin
input = stdin.readline


def main():
  A, B = list(map(int, input().split()))

  print(A*B//math.gcd(A, B))


if(__name__ == '__main__'):
  main()
