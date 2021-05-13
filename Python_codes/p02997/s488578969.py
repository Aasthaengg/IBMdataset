import sys
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N, K = na()

if K > ((N-1) * (N-2) / 2):
    print(-1)
else:
    M = (N-1) + (N-1) * (N-2) // 2 - K
    print(M)
    for i in range(N-1):
        print(1, (i+2))
    cnt = M - (N-1)
    if cnt == 0:
        exit()
    for i in range(2, N+1):
        for j in range(i+1, N+1):
            cnt -= 1
            print(i, j)
            if cnt == 0:
                break
        if cnt == 0:
            break
