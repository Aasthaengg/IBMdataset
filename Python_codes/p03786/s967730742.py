import sys
input = sys.stdin.readline
from itertools import accumulate


def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def solve(N, A):
    A.sort()
    # Aの左側をすべて取り込む (S[x-1])
    # Aの右側を取り込めるところまで取り込む
    S = list(accumulate(A))
    ans = 1
    for i in range(N-2, -1, -1):
        if S[i] * 2 >= A[i+1]:
            ans += 1
        else:
            break
    return ans


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
