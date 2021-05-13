import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, m = input_int_list()
    max_gcd = m // n
    while max_gcd > 1:
        if (m - max_gcd) % max_gcd == 0 and (m - max_gcd) // max_gcd >= n - 1:
            print(max_gcd)
            return
        else:
            max_gcd -= 1
    print(1)
    return


if __name__ == "__main__":
    main()
