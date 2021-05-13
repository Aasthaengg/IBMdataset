#!python3

import numpy as np


# input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


def main():
    a = np.array(sorted(A))
    b = np.array(sorted(B))
    c = np.array(sorted(C))
    
    w = [None] * N
    for i in range(N):
        w[i] = N - np.searchsorted(c, b[i], side="right")
    
    wsum = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        wsum[i] = w[i] + wsum[i + 1]
    
    ans = 0
    for i in range(N):
        ans += wsum[np.searchsorted(b, a[i], side="right")]
    print(ans)


if __name__ == "__main__":
    main()
