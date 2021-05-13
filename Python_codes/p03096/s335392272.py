#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
  value = 1
  skips = {}
  prev = -1

  for _ in range(int(input())):
    n = int(input())

    if n == prev:
      continue

    prev = n

    if n in skips:
      value += skips[n]

    skips[n] = value

  print(value % int(1e+9 + 7), flush=True)


if __name__ == '__main__':
  main()

