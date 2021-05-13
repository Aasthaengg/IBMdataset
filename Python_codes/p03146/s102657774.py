import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    s = ni()
    d = {}
    d[s] = 1
    ans = 1
    while True:
        ans += 1
        if s % 2 == 0:
            s = s // 2
        else:
            s = 3 * s + 1
        if s in d:
            print(ans)
            return
        else:
            d[s] = 1


if __name__ == '__main__':
    main()
