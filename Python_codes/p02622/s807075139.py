# coding: utf-8
# submission # - User: herp_sy
# https://atcoder.jp/contests/
#
# lang: Python3 (3.8.2)

import math
import statistics
import numpy as np
import queue
import itertools
import functools 

ans = 0
s, t = input(), input()
for p in range(len(s)):
	if s[p] != t[p]:
		ans += 1
print(ans)
