import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N,M = map(int, readline().split())

    if N % 2 == 1:
        for i in range(M):
            print(i + 1, N - i)
    else:
        for i in range(M):
            if i < M / 2:
                print(i + 1, N - i)
            else:
                print(i + 2, N - i)


if __name__ == "__main__":
    main()
