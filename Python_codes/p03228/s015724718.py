###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

A, B, K = mi()
C = [A, B]

turn = 0 #0はAのターン、1はBのターン
for _ in range(K):
  if C[turn] % 2 == 1:
    C[turn] -= 1
  C[turn] //= 2
  C[~turn] += C[turn]
  turn = ~turn

print(C[0], C[1])

