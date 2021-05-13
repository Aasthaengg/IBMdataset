import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))

    op = None
    prev = A[0]
    cnt = 0
    for i in range(1, N):
        if op is None:
            if prev == A[i]:
                continue
            elif prev < A[i]:
                op = "up"
                prev = A[i]
            else:
                op = "down"
                prev = A[i]
        else:
            if op == "up":
                if prev <= A[i]:
                    prev = A[i]
                    continue
                else:
                    cnt += 1
                    op = None
                    prev = A[i]
            else:
                if prev >= A[i]:
                    prev = A[i]
                    continue
                else:
                    cnt += 1
                    op = None
                    prev = A[i]

    cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
