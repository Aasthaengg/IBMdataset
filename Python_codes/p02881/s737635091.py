import math
from sys import stdin
input = stdin.readline


def main():
  N = int(input())

  div = 0
  for i in range(int(math.sqrt(N)), 0, -1):
    if N % i == 0:
      div = i
      break

  print(div - 1 + N//div - 1)


if(__name__ == '__main__'):
  main()
