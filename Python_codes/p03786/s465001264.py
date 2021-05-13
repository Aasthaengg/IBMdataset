import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    ans = 1
    S = sum(A)
    for i in reversed(range(N-1)):
        S -= A[i+1]
        if A[i+1] <= 2*S:
            ans += 1
        else:
            break
    print(ans)


if __name__ == "__main__":
    main()
