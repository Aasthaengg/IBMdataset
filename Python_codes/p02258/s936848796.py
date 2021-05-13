#!/usr/bin/python


def main():
  times = int(input())
  min_rate = int(input())
  maxv = - 10 ** 9
  for _ in range(1, times):
    rate = int(input())

    if rate - min_rate > maxv:
      maxv = rate - min_rate

    if rate < min_rate:
      min_rate = rate

  print(maxv)
  return 0


if __name__ == '__main__':
  main()