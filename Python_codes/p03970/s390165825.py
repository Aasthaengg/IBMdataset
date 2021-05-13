###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

S = input()
rightans = "CODEFESTIVAL2016"

ans = 0
for s, ra in zip(S, rightans):
  if s != ra: ans += 1

print(ans)

