#import itertools
#import fractions
#import numpy as np
#mod = 10**4 + 7
"""def kiri(n,m):
  r_ = n / m
  if (r_ - (n // m)) > 0:
    return (n//m) + 1
  else:
    return (n//m)"""

# Written by NoKnowledgeGG @YlePhan

#import math
#mod = 10**9+7



def main():
  a = int(input())
  b = int(input())
  if a > b:
    print('GREATER')
  elif a < b:
    print('LESS')
  else:
    print('EQUAL')
if __name__ == '__main__':
  main()