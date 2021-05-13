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
"""def kiri(n,m):
  r_ = n / m
  if (r_ - (n // m)) > 0:
    return (n//m) + 1
  else:
    return (n//m)"""
 
def main():
  a,b = map(int,input().split())
  print(int((b-a) * (b-a+1)/2 - b))
  
if __name__ == '__main__':
  main()