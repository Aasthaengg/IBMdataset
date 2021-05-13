# coding: utf-8

def solve(X, Ls):
  c, s = 0, 0
  for L in Ls:
    s += L
    if s > X:
      break
    c += 1
  return c + 1


if __name__ == '__main__':
  _, X = map(int, input().split())
  print(solve(X, map(int, input().split())))