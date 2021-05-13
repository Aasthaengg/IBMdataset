import sys
input = sys.stdin.readline
from itertools import accumulate


def read():
    N = int(input().strip())
    S = input().strip()
    return N, S


def solve(N, S):
    W = [0] * (N+1)  # W[j]-W[i]: 区間[i, j)の白の数
    B = [0] * (N+1)  # B[j]-B[i]: 区間[i, j)の黒の数
    for i in range(N):
        s = S[i]
        W[i+1] = W[i] + 1 if s == "." else W[i]
        B[i+1] = B[i] + 1 if s == "#" else B[i]
    # i以上を黒に、i未満を白にする
    # .....##### になればOK
    ans = N
    for i in range(N+1):
        b2w = W[N] - W[i]
        w2b = B[i] - B[0]
        ans = min(ans, b2w + w2b)
    return ans


if __name__ == '__main__':
    inputs = read()
    print("%d" % solve(*inputs))
