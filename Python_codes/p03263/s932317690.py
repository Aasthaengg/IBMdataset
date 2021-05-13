import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    H, W = map(int, readline().split())
    A = list(list(map(int, readline().split())) for _ in range(H))
    move = []
    for i in range(H):
        for j in range(W - 1):
            if A[i][j] % 2:
                A[i][j] -= 1
                A[i][j + 1] += 1
                move.append([i + 1, j + 1, i + 1, j + 2])
    for i in range(H - 1):
        if A[i][W - 1] % 2:
            A[i][W - 1] -= 1
            A[i + 1][W - 1] += 1
            move.append([i + 1, W, i + 2, W])
    print(len(move))
    for m in move:
        print(m[0],m[1],m[2],m[3])


if __name__ == '__main__':
    main()
