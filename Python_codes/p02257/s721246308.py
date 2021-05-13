#coding: UTF-8

import sys
import math

class Algo:
  @staticmethod
  def is_prime(n):
    if n == 2:
      return True
    elif n<2 or n%2 == 0:
      return False
    else:
      for i in range(3,int(math.sqrt(n))+2, 2):
        if n%i == 0:
          return False
    return True

N = int(input())
ans = 0
for i in range(0,N):
  if Algo.is_prime(int(input())):
    ans += 1
print(ans)