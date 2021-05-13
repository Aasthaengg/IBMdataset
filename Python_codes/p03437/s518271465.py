###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

X, Y = mi()

if X % Y == 0:
  print(-1)
else: print(X)

