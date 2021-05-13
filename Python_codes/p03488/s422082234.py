import sys

sys.setrecursionlimit(10000)
INF = float('inf')

S = input()
X, Y = list(map(int, input().split()))


def turn(d):
    return 'x' if d == 'y' else 'y'


i = 0
while i < len(S) and S[i] == 'F':
    i += 1
xs = {i}
ys = {0}
direction = 'x'
while i < len(S):
    while i < len(S) and S[i] == 'T':
        direction = turn(direction)
        i += 1
    cnt = 0
    while i < len(S) and S[i] == 'F':
        i += 1
        cnt += 1
    if direction == 'x':
        xs = {x + cnt for x in xs} | {x - cnt for x in xs}
    else:
        ys = {y + cnt for y in ys} | {y - cnt for y in ys}
if X in xs and Y in ys:
    print('Yes')
else:
    print('No')
