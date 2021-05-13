import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if sorted(p[i - 1 : i + 2])[1] == p[i]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
