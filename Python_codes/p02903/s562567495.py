import sys

input = sys.stdin.readline


def main():
    H, W, A, B = map(int, input().split())

    line = [0] * A + [1] * (W - A)
    X = "".join(map(str, line))
    ans = [""] * H
    for i in range(H):
        if i == B:
            X = "".join(map(lambda x: str(x ^ 1), line))
        ans[i] = X

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
