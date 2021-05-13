import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

sx, sy, tx, ty = mapint()
ans = ''

ans += 'U'*(ty-sy) + 'R'*(tx-sx)
ans += 'D'*(ty-sy) + 'L'*(tx-sx)
ans += 'L'+'U'*(ty-sy+1)+'R'*(tx-sx+1)+'D'
ans += 'R'+'D'*(ty-sy+1) + 'L'*(tx-sx+1)+'U'

print(ans)