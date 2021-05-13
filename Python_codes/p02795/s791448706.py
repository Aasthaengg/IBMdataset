# A - Painting
import sys

debug = lambda message: print("DEBUG:", message, file=sys.stderr)


def main():
    H, W, N = map(int, open(0))
    debug(max(H, W))
    print((N + max(H, W) - 1) // max(H, W))


if __name__ == "__main__":
    main()
