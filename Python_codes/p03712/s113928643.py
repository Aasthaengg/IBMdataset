import sys
input = sys.stdin.readline


def read():
    H, W = map(int, input().strip().split())
    A = []
    for i in range(H):
        a = list(input().strip())
        A.append(a)
    return H, W, A


def solve(H, W, A):
    B = [["#" for j in range(W+2)] for i in range(H+2)]
    for i in range(H):
        for j in range(W):
            B[i+1][j+1] = A[i][j]
    for i in range(H+2):
        print("".join(B[i]))


if __name__ == '__main__':
    inputs = read()
    solve(*inputs)
