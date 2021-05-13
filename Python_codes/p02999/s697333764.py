# coding: utf-8

def solve(X, A):
  return (X >= A) * 10


if __name__ == '__main__':
  print(solve(*map(int, input().split())))