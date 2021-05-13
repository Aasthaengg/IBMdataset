import sys
from collections import Counter, deque
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    res = []
    for h in range(H):
        for w in range(W) if h % 2 == 0 else reversed(range(W)):
            if h % 2 == 0:
                if A[h][w] % 2:
                    if w == W - 1:
                        if h == H - 1:
                            continue
                        else:
                            A[h][w] -= 1
                            A[h + 1][w] += 1
                            res.append([h + 1, w + 1, h + 2, w + 1])
                    else:
                        A[h][w] -= 1
                        A[h][w + 1] += 1
                        res.append([h + 1, w + 1, h + 1, w + 2])
            else:
                if A[h][w] % 2:
                    if w == 0:
                        if h == H - 1:
                            continue
                        else:
                            A[h][w] -= 1
                            A[h + 1][w] += 1
                            res.append([h + 1, w + 1, h + 2, w + 1])
                    else:
                        A[h][w] -= 1
                        A[h][w - 1] += 1
                        res.append([h + 1, w + 1, h + 1, w])
    print(len(res))
    for i in res:
        print(*i)



if __name__ == '__main__':
    resolve()
