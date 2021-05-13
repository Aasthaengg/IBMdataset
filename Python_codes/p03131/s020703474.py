import sys

input = sys.stdin.readline


def main():
    K, A, B = map(int, input().split())

    if A + 2 < B:
        if A - 1 <= K:
            K -= (A - 1)
            ans = A
            q, r, = divmod(K, 2)
            ans += (B - A) * q + r
        else:
            ans = 1 + K
    else:
        ans = 1 + K

    print(ans)


if __name__ == "__main__":
    main()
