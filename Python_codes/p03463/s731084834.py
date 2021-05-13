###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

N,A, B = mi()

if (B-A-1)%2 == 0: print('Borys')
else: print('Alice')
