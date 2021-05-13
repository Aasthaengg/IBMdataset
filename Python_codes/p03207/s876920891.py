import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    A = []
    for _ in range(n):
        A.append(input_int())
    A = sorted(A)
    A[-1] = A[-1] // 2
    print(sum(A))
    return


if __name__ == "__main__":
    main()
