import sys
buf = sys.stdin.buffer


def main():
    n = int(buf.readline())
    A = list(map(int, buf.readline().split()))
    A.sort()
    print(A[n-1] - A[0])


if __name__ == "__main__":
    main()