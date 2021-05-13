###template###
import sys
input = sys.stdin.readline
def mi(): return map(int, input().split())
###template###

N, A, B = mi()
ans = [0,0]
ans[0] = min(A,B)
ans[1] = max(A+B-N,0)

print(ans[0], ans[1])

