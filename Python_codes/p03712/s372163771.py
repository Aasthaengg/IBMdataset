#!python3

LI = lambda: list(map(int, input().split()))

# input
H, W = LI()
A = ["#" + input() + "#" for _ in range(H)]


def main():
    x = ["#" * (W + 2)]
    ans = x + A + x
    print("\n".join(ans))


if __name__ == "__main__":
    main()
