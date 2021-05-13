import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = [0] * N
    for i in range(N):
        A[i] = int(input())

    ans = 0
    prev_a = -1
    for i, a in enumerate(A):
        if (a > i) or (a > prev_a + 1):
            ans = -1
            break

        if a > 0:
            ans += 1
            if prev_a + 1 != a:
                ans += (a - 1)

        prev_a = a

    print(ans)


if __name__ == "__main__":
    main()
