import sys

input = sys.stdin.readline


def main():
    N = int(input())

    L = len(str(N))
    ans = sum(map(int, str(N)))

    for d in range(L):
        if str(N)[d] == "0":
            continue
        m = sum(map(int, str(N)[:d + 1])) - 1 + 9 * (L - (d + 1))
        if m > ans:
            ans = m

    print(ans)


if __name__ == "__main__":
    main()
