#!python3

LI = lambda: list(map(int, input().split()))

# input
N = int(input())
K = int(input())
X = LI()


def main():
    ans = 0
    for x in X:
        ans += 2 * min(x - 0, K - x);
    print(ans)


if __name__ == "__main__":
    main()
