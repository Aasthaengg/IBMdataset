import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    status = "undefined"
    ans = 1
    for i in range(N - 1):
        diff = A[i + 1] - A[i]
        if status == "undefined":
            if diff == 0:
                pass
            elif diff > 0:
                status = "increase"
            else:
                status = "decrease"
        elif status == "increase":
            if diff >= 0:
                pass
            else:
                ans += 1
                status = "undefined"
        else:
            if diff <= 0:
                pass
            else:
                status = "undefined"
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
