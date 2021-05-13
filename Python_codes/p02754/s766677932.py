import sys


def main():
    input = sys.stdin.buffer.readline
    n, a, b = map(int, input().split())
    if a + b == 0:
        print(0)
    else:
        q, mod = divmod(n, a + b)
        print(q * a + min(mod, a))


if __name__ == "__main__":
    main()
