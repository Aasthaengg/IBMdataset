# coding: utf-8

from functools import reduce

def solve(X, Ls):
  return len(list(filter(
    lambda x: x <= X, reduce(lambda x, y: x + [x[-1] + y], Ls, [0]))))


if __name__ == '__main__':
  _, X = map(int, input().split())
  print(solve(X, map(int, input().split())))