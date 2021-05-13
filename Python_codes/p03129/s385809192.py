###template###
import sys
input = sys.stdin.readline
def mi(): return map(int, input().split())
###template###

N, K = mi()

if N >= (K*2 - 1):
  print('YES')
else: print('NO')

