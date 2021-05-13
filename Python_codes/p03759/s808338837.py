###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

a, b, c = mi()

if b-a==c-b: print('YES')
else: print('NO')


