#!/usr/bin/python3
# -*- coding:utf-8 -*-

from collections import defaultdict
import bisect

def main():
  s = input().strip()
  t = input().strip()
  ns = len(s)
  
  if len(set(list(t)) - set(list(s))):
    print(-1)
    return
  
  ichs = defaultdict(list)  
  for i, c in enumerate(s):
    ichs[c].append(i)
    
  ic = -1
  cnt = 0
  for c in t:
    ix = bisect.bisect_right(ichs[c], ic)
    
    if ix >= len(ichs[c]):
      cnt += 1
      ix = 0
    else:
      if ic == ichs[c][ix]:
        if ix + 1 >= len(ichs[c]):
          cnt += 1
          ix = 0
        else:
          ix += 1
    ic = ichs[c][ix]
  print(cnt*ns + ic + 1)
    
      
    
  

if __name__=='__main__':
  main()

