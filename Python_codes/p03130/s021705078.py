###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

a = list(mi()) + list(mi()) + list(mi())
cnts = [a.count(i) for i in range(1,5)]

if max(cnts) == 3: print('NO')
else: print('YES')

