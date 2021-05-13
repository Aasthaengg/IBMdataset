from sys import stdin
input = stdin.readline


def main():
  from math import gcd
  K = int(input())

  sum_ = 0
  for a in range(1, K+1):
    for b in range(1, K+1):
      for c in range(1, K+1):
        sum_ += gcd(gcd(a, b), c)

  print(sum_)


if(__name__ == '__main__'):
  main()
