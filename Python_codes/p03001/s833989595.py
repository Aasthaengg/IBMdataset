# coding: utf-8

def solve(W, H, x, y):
  mw, mh = W / 2, H / 2
  return f'{W * H / 2} {int((x, y) == (mw, mh))}'


if __name__ == '__main__':
  print(solve(*map(int, input().split())))