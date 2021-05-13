#!python3

LI = lambda: list(map(int, input().split()))

# input
N = int(input())
A = [LI() for _ in range(N)]


def main():
    ans = 0
    for i in range(N):
        for j in range(N):
            flag = True
            for k in range(N):
                if i == k or j == k:
                    continue
                d = A[i][k] + A[k][j]
                if A[i][j] > d:
                    print(-1)
                    return
                if A[i][j] == d:
                    flag = False
            if flag:
                ans += A[i][j]
    ans //= 2
    print(ans)


if __name__ == "__main__":
    main()
