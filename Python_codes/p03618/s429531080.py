from collections import Counter


def main():
    A = input()
    N = len(A)
    c = Counter(A)
    print(1 + N * (N - 1) // 2 - sum([v * (v - 1) // 2 for v in c.values()]))


if __name__ == '__main__':
    main()