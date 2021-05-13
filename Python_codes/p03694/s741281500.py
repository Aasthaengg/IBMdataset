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
  n = int(input())
  a = list(map(int,input().split()))
  a = sorted(a,reverse=True)
  print(a[0] - a[n-1])
  
  
if __name__ == '__main__':
  main()