#coding: UTF-8

import sys

class Algo:
  @staticmethod
  def greatest_common_divisor(x, y):
    while True:
      r = x%y
      if r==0:
        print(y)
        break
      x, y = y, r
l = list(map(int, input().split()))
X = l[0]
Y = l[1]
Algo.greatest_common_divisor(X, Y)