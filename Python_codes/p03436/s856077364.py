from collections import deque
def main():
    H, W = list(map(int, input().split()))
    A = [['#'] * (W + 2)] + [['#', ] + list(input()) + ['#', ] for _ in range(H)] + [['#'] * (W + 2)]
    printl = lambda l: [print(x) for x in l]
    stack = deque([[1, 1], ])
    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    INF = float('inf')
    L = [[INF] * W for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    L[0][0] = 1
    while stack:
        x, y = stack.popleft()
        if visited[x - 1][y - 1] == 1:
            continue
        visited[x - 1][y - 1] = 1
        for (dx, dy) in dxy:
            X = x + dx
            Y = y + dy
            if A[X][Y] == '#':
                continue
            if visited[X - 1][Y - 1] == 0:
                stack.append([X, Y])
            L[X - 1][Y - 1] = min(L[X - 1][Y - 1], L[x - 1][y - 1] + 1)
    ans = 0
    for a in A:
        for i in a:
            if i == '.':
                ans += 1
    if L[H - 1][W - 1] == INF:
        print(-1)
    else:
        print(ans - L[H - 1][W - 1])

if __name__ == '__main__':
    main()
