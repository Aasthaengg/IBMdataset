import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    odd_product = 1
    for a in A:
        if a % 2 == 0:
            count = 2
        else:
            count = 1
        odd_product *= count

    ans = 3 ** N - odd_product
    print(ans)


if __name__ == "__main__":
    main()
