#
# Written by NoKnowledgeGG @YlePhan
# ('ω')
#
#import math
#mod = 10**9+7
#import itertools
#import fractions
#import numpy as np
#mod = 10**4 + 7
def kiri(n,m):
  r_ = n / m
  if (r_ - (n // m)) > 0:
    return (n//m) + 1
  else:
    return (n//m)
  
def main():
  n,d = map(int,input().split())
  d = d*2 + 1
  print(kiri(n,d))
  
if __name__ == '__main__':
  main()