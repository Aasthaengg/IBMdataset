import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    dif = 999
    ans = ''
    for i in range(1, 10):
        tmp = str(i) * 3
        if dif > int(tmp) - n >= 0:
            dif = abs(n - int(tmp))
            ans = tmp
    print(ans)


if __name__ == '__main__':
    main()
