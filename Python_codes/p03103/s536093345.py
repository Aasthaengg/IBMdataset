import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, m = nm()
    AB = [tuple(map(int, input().split())) for _ in range(n)]
    AB = sorted(AB, key=lambda x: x[0])
    num = 0
    ans = 0
    for a, b in AB:
        w_num = m - num
        if w_num <= b:
            num += w_num
            ans += w_num * a
            break
        else:
            num += b
            ans += b * a
    print(ans)


if __name__ == '__main__':
    main()