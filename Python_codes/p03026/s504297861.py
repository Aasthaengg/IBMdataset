#!/usr/bin/env python

from collections import deque
import itertools as ite
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

N = input()
E = [[] for i in range(N + 1)]

for i in range(N - 1):
	a, b = map(int, raw_input().split())
	E[a].append(b)
	E[b].append(a)

c = map(int, raw_input().split())
c.sort(reverse = True)
print sum(c[1:])

ans = [0] * (N + 1)
def func(pos, pre, id):
	ans[pos] = c[id]
	id += 1
	for to in E[pos]:
		if to != pre:
			id = func(to, pos, id)
	return id

func(1, -1, 0)
print " ".join(map(str, ans[1:]))