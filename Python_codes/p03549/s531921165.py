def main():
    N, M = map(int, input().split())

    unit = M * 1900 + (N - M) * 100
    ans = unit * (1 << M)

    print(ans)


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
