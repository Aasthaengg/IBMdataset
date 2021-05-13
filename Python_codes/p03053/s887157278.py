import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    H, W = [int(x) for x in input().split()]
    A = [input().strip() for _ in range(H)]

    q = collections.deque()

    ans = [[0] * W for j in range(H)]

    for j in range(H):
        for i in range(W):
            if A[j][i] == '#':
                q.append((j, i, 0))
                ans[j][i] = -1

    while q:
        c = q.popleft()
        y, x, d = c[0], c[1], c[2]
        for ny, nx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if 0 <= y + ny < H and 0 <= x + nx < W:
                if ans[y + ny][x + nx] == 0:
                    ans[y + ny][x + nx] = d + 1
                    q.append((y + ny, x + nx, d + 1))

    a = 0
    for aa in ans:
        a = max(a, max(aa))
    print(a)


if __name__ == '__main__':
    main()
