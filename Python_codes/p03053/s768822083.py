from collections import deque


def resolve():
    H, W = map(int, input().split())
    A, q = [], deque([])
    for i in range(H):
        A.append(list(input()))
        if '#' in A[i]:
            for j in range(W):
                if A[i][j] == '#':
                    q.append((i, j))

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    cnt = -1

    # 1回目で各黒マスを拡張して，2回目以降は拡張した黒マスから拡張してく
    nq = deque([])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and A[ny][nx] == '.':
                nq.append((ny, nx))
                A[ny][nx] = '#'
        if q == deque([]):
            q = nq
            nq = deque([])
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    resolve()