import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


def main():
    k = int(input())
    cur = 0

    for i in range(1, 10 ** 7):
        cur *= 10
        cur += 7
        cur %= k

        if cur == 0:
            print(i)
            return
    print(-1)


if __name__ == '__main__':
    main()