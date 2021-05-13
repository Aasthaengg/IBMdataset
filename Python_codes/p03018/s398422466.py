import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    ans = 0
    A_count = 0
    i = 0
    N = len(S)
    while i < N - 1:
        if S[i] == "A":
            A_count += 1
            i += 1
        elif S[i:i + 2] == "BC":
            ans += A_count
            i += 2
        else:
            A_count = 0
            i += 1

    print(ans)


if __name__ == "__main__":
    main()
