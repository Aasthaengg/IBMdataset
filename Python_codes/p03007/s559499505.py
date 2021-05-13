import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main():
    N = II()
    A = LI()

    A.sort()
    from bisect import bisect
    slice_ = bisect(A, 0)
    from collections import deque
    minus = deque(A[:slice_])
    plus = deque(A[slice_:])
    # print(minus, plus)

    if minus and plus:
        first_plus = plus.popleft()
        first_minus = minus.popleft()
    elif minus and not plus:
        first_plus = minus.pop()  # must be the max of minuses
        first_minus = minus.popleft()
    elif plus and not minus:
        first_minus = plus.popleft()  # must be the min of pluses
        first_plus = plus.popleft()

    # first_plus - (first_minus - plus - plus - ...) - minus - minus - ...
    tmp = first_minus
    ans_li = []
    while len(plus) > 0:
        p = plus.popleft()
        ans_li.append((tmp, p))
        tmp = tmp - p
    ans_li.append((first_plus, tmp))
    tmp = first_plus - tmp
    while len(minus) > 0:
        m = minus.popleft()
        ans_li.append((tmp, m))
        tmp = tmp - m
    print(tmp)
    for i in ans_li: print('{} {}'.format(*i))


main()