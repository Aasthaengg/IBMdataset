import sys
def input():
    return sys.stdin.readline()[:-1]


def main():
    A, B, N = map(int,input().split())
    if B - 1 <= N:
        print(A * (B - 1) // B)
    else:
        print(A * N // B)


if __name__ == "__main__":
    main()