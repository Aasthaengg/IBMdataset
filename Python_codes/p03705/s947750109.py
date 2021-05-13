import sys

input = sys.stdin.readline


def main():
    N, A, B = map(int, input().split())

    if A > B:
        ans = 0
    elif N == 1:
        if A == B:
            ans = 1
        else:
            ans = 0
    else:
        min_sum = A * (N-2)
        max_sum = B * (N-2)
        ans = max_sum - min_sum + 1
    print(ans)


if __name__ == "__main__":
    main()
