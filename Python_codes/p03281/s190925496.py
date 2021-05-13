import sys


def yakusu(i):

    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1

    return cnt


def main():
    N = int(sys.stdin.readline().rstrip())

    cnt = 0
    for i in range(1, N + 1):
        if yakusu(i) == 8 and i % 2 == 1:
            cnt += 1

    print(cnt)


main()
