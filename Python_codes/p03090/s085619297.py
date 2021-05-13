import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    N = int(input())
    answer = []
    if N % 2 == 1:
        for i in range(1, N):
            answer.append((N, i))
        for j in range(1, N):
            for k in range(j + 1, N):
                if j + k == N:
                    continue
                else:
                    answer.append((j, k))
    else:
        for i in range(2, N):
            answer.append((N, i))
            answer.append((1, i))
        for j in range(2, N):
            for k in range(j + 1, N):
                if j + k == N + 1:
                    continue
                else:
                    answer.append((j, k))
    M = len(answer)
    print(M)
    for i in range(M):
        print(*answer[i], sep=" ")


if __name__ == "__main__":
    main()
