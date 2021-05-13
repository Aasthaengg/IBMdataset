import sys


def slove():
    input = sys.stdin.readline
    n, t = list(map(int, input().rstrip('\n').split()))
    tl = list(map(int, input().rstrip('\n').split()))
    mt = 0
    for i in range(n-1):
        mt += (min(tl[i] + t, tl[i+1]) - tl[i])
    print(mt + t)


if __name__ == '__main__':
    slove()
