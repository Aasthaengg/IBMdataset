from math import ceil


def main():
    n = int(input())
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    added = 0
    for i in range(n - 1, -1, -1):
        added += ceil((a[i] + added) / b[i]) * b[i] - (a[i] + added)
    print(added)


if __name__ == '__main__':
    main()

