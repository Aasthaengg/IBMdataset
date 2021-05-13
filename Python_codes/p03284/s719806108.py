import sys

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    if n % k == 0:
        print(0)
    else:
        p = [0] * k
        for i in range(n):
            p[i % k] += 1
        print(max(p) - min(p))


if __name__ == "__main__":
    main()
