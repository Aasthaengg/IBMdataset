import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

sx, sy, tx, ty = map(int, input().split())

tx -= sx
ty -= sy

s = str()
s += 'R' * tx
s += 'U' * ty
s += 'L' * tx
s += 'D' * (ty + 1)
s += 'R' * (tx + 1)
s += 'U' * (ty + 1)
s += 'L'
s += 'U'
s += 'L' * (tx + 1)
s += 'D' * (ty + 1)
s += 'R'

print (s)