
import math
from sys import stdin
input = stdin.readline


def main():
  A, B, C = list(map(int, input().split()))

  print("NO" if C % math.gcd(A, B) else "YES")


if(__name__ == '__main__'):
  main()