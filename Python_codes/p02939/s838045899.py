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
    tmp = ""
    prev = ""
    cnt = 0
    for s in S:
        tmp += s
        if tmp != prev:
            cnt += 1
            prev = tmp
            tmp = ""
        elif tmp == prev:
            continue

    print(cnt)

    return


if __name__ == "__main__":
    main()
