import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


n, m, d = MI()


def s():
    # a = n
    # if n - 2 * d >= 0:
    #     a += n - 2 * d
    # else:
    #     a += n - 2 * d
    # return a
    if d == 0:
        return 1
    return 2 * (n - d) / n

print(s() * (m - 1) / n)