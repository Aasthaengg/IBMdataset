import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    S = input()
    for i in range(ord("a"), ord("z") + 1):
        if chr(i) not in S:
            print(chr(i))
            return
    print("None")
    return


if __name__ == "__main__":
    main()
