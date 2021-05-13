from itertools import groupby
import sys
rr = lambda: sys.stdin.readline().rstrip()
s = rr()
print('Good' if len(list(groupby(s))) == 4 else 'Bad')














