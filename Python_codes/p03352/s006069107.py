import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    x = ni()
    d = x
    ans = 1
    for i in range(2, 33):
        j = 2
        while pow(i, j) <= x:
            if d > x - pow(i, j):
                ans = pow(i, j)
                d = x - pow(i, j)
            j += 1
    print(ans)


if __name__ == '__main__':
    main()
