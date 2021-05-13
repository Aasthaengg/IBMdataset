import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def read():
    H, W = map(int, input().strip().split())
    C = []
    for i in range(H):
        c = input().strip()
        C.append(c)
    return H, W, C


def solve(H, W, C):
    for c in C:
        print(c)
        print(c)


if __name__ == '__main__':
    inputs = read()
    solve(*inputs)
