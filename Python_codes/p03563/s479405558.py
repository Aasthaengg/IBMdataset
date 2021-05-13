def main():
    R = int(input())
    G = int(input())

    for x in range(-9 * 10 ** 3, 9 * 10 ** 3 + 1):
        if R + x == G * 2:
            print(x)
            return

    print(-1)


if __name__ == '__main__':
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())
