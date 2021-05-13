import sys
import numpy as np
input = lambda: sys.stdin.readline().rstrip()
INF = 10**9 + 1


def solve():
    N, K = map(int, input().split())
    S = np.array(list(input()), dtype='str')

    if N == 1:
        print(0)
        exit()

    ri = INF
    kc = 0
    fs = S[0]
    if fs == 'R':
        nfs = 'L'
    else:
        nfs = 'R'

    for i in range(N):
        if S[i] == nfs:
            ri = min(ri, i)
        elif S[i] == fs and ri != INF:
            S[ri:i] = fs
            ri = INF
            kc += 1
            if kc == K:
                break
    else:
        if ri != INF and S[-1] == nfs:
            S[ri:N] = fs

    # print(S)

    happy = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            happy += 1

    print(happy)


if __name__ == '__main__':
    solve()
