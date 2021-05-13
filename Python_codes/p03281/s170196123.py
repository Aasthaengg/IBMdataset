import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            cnt[j] += 1
    ans = len([i for i in range(1, n + 1, 2) if cnt[i] == 8])
    print(ans)


if __name__ == "__main__":
    main()
