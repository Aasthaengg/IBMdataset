#!python3

LI = lambda: list(map(int, input().split()))

# input
N, M = LI()


def main():
    s = N
    c = M
    x = min(s, c // 2)
    c -= 2 * x
    y = c // 4
    ans = x + y
    print(ans)
    


if __name__ == "__main__":
    main()
