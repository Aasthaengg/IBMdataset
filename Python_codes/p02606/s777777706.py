import sys


def main():
    input = sys.stdin.buffer.readline
    l, r, d = map(int, input().split())
    ans = 0
    for i in range(l, r + 1):
        if i % d == 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
