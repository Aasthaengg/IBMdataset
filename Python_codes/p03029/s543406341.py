import sys

input = sys.stdin.readline


def main():
    A, P = map(int, input().split())
    q, _ = divmod(3 * A + P, 2)
    print(q)


if __name__ == "__main__":
    main()
