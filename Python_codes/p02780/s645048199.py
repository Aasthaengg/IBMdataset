import sys


def main():
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    s = sum(p[:k])
    max_sum = s
    for i in range(k, n):
        s += p[i]
        s -= p[i - k]
        max_sum = max(max_sum, s)
    print((k + max_sum) / 2)


if __name__ == "__main__":
    main()
