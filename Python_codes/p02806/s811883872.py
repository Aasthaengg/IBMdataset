import math
import sys
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    stList = [list(map(str, readline().rstrip().split())) for _ in range(n)]
    x = readline().rstrip()
    sumT = 0
    flg = False

    for i in range(n):
        s, t = stList[i][0], int(stList[i][1])
        if flg != True:
            if s == x:
                flg = True
                continue
        if flg == False:
            continue
        sumT += t
    print(sumT)


if __name__ == '__main__':
    main()
