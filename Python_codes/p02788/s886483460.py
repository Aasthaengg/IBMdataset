import sys
from operator import itemgetter
from collections import deque


def solve():
    N, D, A = map(int, sys.stdin.readline().split())
    m = map(int, sys.stdin.read().split())
    XH = sorted(list(zip(m, m)), key=itemgetter(0))
    H = deque()
    X = deque()
    h_popleft = H.popleft
    x_popleft = X.popleft
    h_append = H.append
    x_append = X.append
    count = 0
    num = 0
    for x, h in XH:
        while X and X[0] < x:
            x_popleft()
            num -= (h_popleft() + (A - 1)) // A
        h -= A * num
        if h > 0:
            count += (h + (A - 1)) // A
            x_append(x + D*2)
            h_append(h)
            num += (h + (A - 1)) // A
    return count


if __name__ == '__main__':
    answer = solve()
    print(answer)
