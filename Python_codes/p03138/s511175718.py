import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, input().rstrip('\n').split()))
    a = list(map(int, input().rstrip('\n').split()))
    ls = [0] * 45
    for v in a:
        d = 0
        while True:
            bt = v >> d
            if bt != 0:
                ls[d] += bt & 1
                d += 1
            else:
                break
    t = 0
    for i in range(44, -1, -1):
        if n / 2 >= ls[i]:
            t += 2 ** i
            if t > k:
                t -= 2 ** i
    ans = 0
    for v in a:
        ans += v ^ t
    print(ans)


if __name__ == '__main__':
    solve()
