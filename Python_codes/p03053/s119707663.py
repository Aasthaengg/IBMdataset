import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)

def solve():
    H, W = map(int, input().split())
    M = [[] for _ in range(H)]
    queue = deque()
    for i in range(H):
        M[i] = list(input())
        for j in range(W):
            if M[i][j] == '#':
                queue.append((i, j))
    ans = 0
    while queue:
        # 今の地点から1ステップ変化
        n = len(queue)
        flag = False
        for _ in range(n):
            cy, cx = queue.popleft()
            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= nx < W and 0 <= ny < H and M[ny][nx] == '.':
                    M[ny][nx] = '#'
                    flag = True
                    queue.append((ny, nx))
        if flag:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
