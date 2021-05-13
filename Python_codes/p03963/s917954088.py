def main():
    N, K = map(int, input().split())

    ret = K
    for _ in range(N - 1):
        ret *= K - 1
    print(ret)


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
