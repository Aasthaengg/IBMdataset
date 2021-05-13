from math import *


def f(deg):
  di = radians(90)
  turn = radians(deg)
  i = 1
  x = 0
  y = 1
  while not done(x, y):
    di += turn
    i += 1
    y += sin(di)
    x += cos(di)
    # print(x, y, i, di)
  return i


def done(x, y):
  return abs(x - 0) < 0.00001 and abs(y - 0) < 0.00001

print(f(int(input())))