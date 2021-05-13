import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    K, A, B = map(int, input().split())
    if (B - A) <= 2:
        answer = 1 + K
    else:
        cookie = A
        cnt = A - 1
        money = (K - cnt) // 2
        hit = (K - cnt) % 2
        cookie += money * (B - A)
        cookie += hit
        answer = cookie
    print(answer)


if __name__ == "__main__":
    main()
