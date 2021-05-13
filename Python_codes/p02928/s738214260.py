import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))

    count1 = 0
    count2 = 0

    for i in range(N - 1):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                count1 = count1 + 1
            if A[i] != A[j]:
                count2 = count2 + 1
    count1 = count1 * K
    count2 = count2 * (K * (K - 1) // 2)

    ans = (count1 + count2) % 1000000007
    print(ans)


if __name__ == "__main__":
    main()