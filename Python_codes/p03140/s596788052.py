###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

N = int(input())
A = input()
B = input()
C = input()

ans = 0
for a, b, c in zip(A, B, C):
  ans += len(set((a,b,c)))-1

print(ans)

