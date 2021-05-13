import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    sx, sy, tx, ty = input_int_list()
    dx, dy = tx - sx, ty - sy
    ans = "R" * dx + "U" * dy + "L" * dx + "D" * dy + "L" + "U" * (dy + 1) + "R" * (dx + 1) + "DR" + "D" * (dy + 1) + "L" * (dx + 1) + "U"
    print(ans)
    return


if __name__ == "__main__":
    main()
