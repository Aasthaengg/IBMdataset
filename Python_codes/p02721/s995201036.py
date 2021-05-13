#!python3

iim = lambda: map(int, input().rstrip().split())
from collections import defaultdict

def resolve():
    N, K, C = iim()
    S = input()

    C1 = C+1
    i, cnt, ax = N-1, 0, [0] * K
    while i >= 0:
        if S[i] != "o":
            i -= 1
        else:
            cnt += 1
            ax[K-cnt] = i
            i -= C1
            if cnt == K:
                break

    ans, ri, cnt, i  = [], len(ax)-1, 0, 0
    while i < N:
        if S[i] != "o":
            i += 1
        else:
            if i == ax[cnt]:
                ans.append(i+1)
            i += C1
            cnt += 1
            if cnt == K:
                break
    print(*ans, sep="\n")

if __name__ == "__main__":
    resolve()
