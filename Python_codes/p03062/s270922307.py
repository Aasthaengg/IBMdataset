import math


def main():
    n = int(input())
    # a, b, t = map(int, input().split())
    # h = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in rane(n)]

    a = list(map(int, input().split()))
    abs_a = []
    minus = 0
    for ai in a:
        if ai < 0:
            minus += 1
        abs_a.append(abs(ai))

    if minus % 2 == 0:
        print(sum(abs_a))
    else:
        mini = min(abs_a)
        print(sum(abs_a) - 2*mini)


if __name__ == '__main__':
    main()
