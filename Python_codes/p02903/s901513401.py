import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    H, W, A, B = map(int, readline().split())
    L = [[0]*W for _ in range(H)]
    for h in range(B):
        for w in range(A,W):
            L[h][w] = 1
    for h in range(B,H):
        for w in range(A):
            L[h][w] = 1
    for l in L:
        print(''.join(map(str,l)))
    


if __name__ == '__main__':
    main()
