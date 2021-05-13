# -*- coding: utf-8 -*-
import sys;
import string;
sys.setrecursionlimit(20000) # 再起呼び出しの最大数をセット

import copy
import itertools

from functools import lru_cache
#@lru_cache(maxsize = None)

PPP = 1000000007

# 整数の入力
#n = int(input())

# スペース区切りの整数の入力
#w = [x for x in map(int, input().split())]
n, k = map(int, input().split())
print("sp", n, k, file=sys.stderr)
#p, q, r = map(int, input().split())

# 改行区切りの整数の入力
a = []
#for x in range(m):
#  a.append(int(input()))
#  a.append([int(x) for x in input().split()])
#p = [int(x) for x in input().split()]
#print(a, file=sys.stderr)

# 文字列の入力
#s = input()

# 出力
#print("{} {}".format(a+b+c, s))
#a.sort()
#print(set(a), file=sys.stderr)
#print(len(set(a)))

#cache = dict()

import re

def doit():
  if k == 1:
    return 0
  return n - k

#print(doit([0] * 4))
#doit(s)
try:
  print(doit())
except Exception as e:
  print("e", e, file=sys.stderr)
