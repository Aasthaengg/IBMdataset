# -*- coding: utf-8 -*-

#############
# Libraries #
#############

import sys
input = sys.stdin.readline

N = int(input())
S = list(input())
Q = int(input())


alphabet = "abcdefghijklmnopqrstuvwxyz"

bag = { l:[] for l in alphabet}

for i in range(N):
  bag[S[i]].append(i+1)


import bisect

for _ in range(Q):
  t,a,b = input().split()
  a = int(a)
  if int(t) == 1:
    if S[a-1]!=b:
      bag[S[a-1]].remove(a)
      S[a-1] = b
      bisect.insort(bag[b],a)
  else:
    count = 0
    b = int(b)
    for l in alphabet:
      if len(bag[l])>0:
        left = bisect.bisect_left(bag[l],a)
        if left != len(bag[l]):
          if bag[l][left] <= b:
            count += 1
    print(count)
