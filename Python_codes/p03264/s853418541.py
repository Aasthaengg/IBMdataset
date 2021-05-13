import sys

input = sys.stdin.readline


def main():
    K = int(input())

    n_odd = 0
    n_even = 0
    for i in range(1, K + 1):
        if i % 2 == 0:
            n_even += 1
        else:
            n_odd += 1
    ans = n_odd * n_even

    print(ans)


if __name__ == "__main__":
    main()
