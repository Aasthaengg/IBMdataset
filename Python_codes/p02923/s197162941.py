import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    move = 0
    for i in range(1, n):
        if h[i] <= h[i - 1]:
            move += 1
            ans = max(ans, move)
        else:
            move = 0
    print(ans)


if __name__ == "__main__":
    main()
