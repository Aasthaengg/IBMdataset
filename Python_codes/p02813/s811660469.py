import itertools


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    lst = sorted(P)

    for i, j in enumerate(itertools.permutations(lst)):
        if list(j) == P:
            a = i
        if list(j) == Q:
            b = i

    print(abs(a - b))


if __name__ == "__main__":
    main()
