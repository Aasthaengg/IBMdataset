#!/usr/bin/python3
# -*- coding:utf-8 -*-

import re

def main():
  s = input().strip()
  s = s.replace('BC', 'X')
  ans = 0
  for ax in re.split(r'[BC]+', s):
    inds = []
    for i in range(len(ax)):
      if ax[i] == 'A':
        inds.append(i)
    ans += sum([len(ax) - 1 - ind for ind in inds]) - sum(range(len(inds)))
  print(ans)

if __name__=='__main__':
  main()

