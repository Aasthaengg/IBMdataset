from sys import stdin, setrecursionlimit


def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    a.insert(0, 0)
    a.append(0)

    max = 0

    for i in range(1, n + 2):
        max += abs(a[i] - a[i - 1])

    for i in range(1, n + 1):
        print(max + abs(a[i + 1] - a[i - 1]) - abs(a[i] - a[i - 1]) - abs(a[i + 1] - a[i]))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()