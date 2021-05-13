# -*- coding: utf-8 -*-
import heapq

a,b,c = map(int, input().split())
l = [a,b,c]
l2 = heapq.nsmallest(3, l)
if (l2[0] + l2[1]) == max(l):
  print('Yes')
else:
  print('No')
