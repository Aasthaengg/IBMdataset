from itertools import groupby
import sys
rr = lambda: sys.stdin.readline().rstrip()

print('Good' if len(list(groupby(rr()))) == 4 else 'Bad')