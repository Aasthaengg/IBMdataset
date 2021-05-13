import sys
import collections
import bisect


def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    cnt = 0
    for i in range(len(ab)):
        cnt += ab[i][1]
        if cnt >= k:
            print(ab[i][0])
            return


if __name__ == '__main__':
    main()
