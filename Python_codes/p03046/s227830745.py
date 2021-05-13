import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


M, K = na()
if 2 ** M <= K:
    print(-1)
    exit()
if M == 1:
    if K == 0:
        print("0 0 1 1")
        exit()
    else:
        print(-1)
        exit()
ans_array = [0] * (2 ** (M+1))

for i in range(2**M-1):
    ans_array[i] = i if i < K else i + 1

ans_array[2**M-1] = K

for i in range(2**M-1, 0, -1):
    ans_array[-(i+1)] = i if i > K else i - 1

ans_array[-1] = K
print(" ".join(map(str, ans_array)))
