from itertools import permutations


def main():
    n = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))

    for i, per in enumerate(permutations(range(1, n + 1), n)):
        if per == P:
            a = i
        if per == Q:
            b = i

    print(abs(a - b))


if __name__ == "__main__":
    main()
