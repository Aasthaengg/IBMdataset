import sys
input = sys.stdin.readline


def main():
    N, M, K = map(int, input().split())
    for i in range(N+1):
        for j in range(M+1):
            if i*M + j*N - 2*min(i, j)*max(i, j) == K:
                print("Yes")
                return
    print("No")


if __name__ == '__main__':
    main()
