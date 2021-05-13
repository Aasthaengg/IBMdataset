import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    answer = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 0:
                continue
            else:
                if h + 1 <= H - 1 and w + 1 <= W - 1:
                    if A[h + 1][w] % 2 == 1:
                        A[h + 1][w] += 1
                        answer.append([h + 1, w + 1, h + 2, w + 1])
                    else:
                        A[h][w + 1] += 1
                        answer.append([h + 1, w + 1, h + 1, w + 2])
                elif h + 1 <= H - 1:
                    A[h + 1][w] += 1
                    answer.append([h + 1, w + 1, h + 2, w + 1])
                elif w + 1 <= W - 1:
                    A[h][w + 1] += 1
                    answer.append([h + 1, w + 1, h + 1, w + 2])
                else:
                    continue
    N = len(answer)
    print(N)
    for i in range(N):
        print(*answer[i], sep=" ")


if __name__ == "__main__":
    main()
