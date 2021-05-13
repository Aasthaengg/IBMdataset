import sys
input = sys.stdin.readline


def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]

    zorome_count = 0
    for d in D:
        if d[0] == d[1]:
            zorome_count += 1
        else:
            zorome_count = 0
        if zorome_count == 3:
            break

    print('Yes' if zorome_count == 3 else 'No')


if __name__ == "__main__":
    main()
