H, W = [int(_) for _ in input().split()]
A = [list(input()) for _ in range(H)]

from collections import deque

lst = deque()

for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            lst.append((i, j, 0))


def chg(i, j):
    if i < 0 or j < 0 or H <= i or W <= j: return False
    if A[i][j] == '.':
        A[i][j] = '#'
        return True
    return False


ans = 0
while lst:
    h, w, v = lst.popleft()
    ans = max(v, ans)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 and j != 0: continue

            if chg(h + i, w + j):
                lst.append((h + i, w + j, v + 1))
print(ans)
