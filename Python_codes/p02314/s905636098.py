#!/usr/bin/env python
import sys
sys.setrecursionlimit(100000000)

n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
DP = {}

# num 番目までのコインを使い、yen 円支払うときに必要な枚数
def func(num, yen):
	if num < 0 or yen < 0:
		return 10 ** 18
	if num == 0 and yen == 0:
		return 0
	if not (num, yen) in DP:
		DP[(num, yen)] = min(func(num - 1, yen), func(num, yen - c[num]) + 1)
	return DP[(num, yen)]

print(func(m - 1, n))

