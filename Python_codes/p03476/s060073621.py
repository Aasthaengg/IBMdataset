import sys
# readline = sys.stdin.readline
read = sys.stdin.read
from itertools import accumulate
from copy import deepcopy
def main():
    maxa2 = 10**5
    p = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(maxa2)]
    p[0] = p[1] = False
    p[2] = p[3] = p[5] = True
    for is1 in range(3, maxa2, 2):
        for is2 in range(is1 ** 2, maxa2, is1):
            p[is2] = False
    p2 = deepcopy(p)
    for i, pe in enumerate(p):
        if pe:
            i2 = ((i + 1) / 2)
            if i2 % 1 != 0:
                p2[i] = False
                continue
            elif not p[int(i2)]:
                p2[i] = False
    p2a = tuple(accumulate(p2))

    q = int(input())
    m = map(int, read().split())
    lr= zip(m, m)
    for l, r in lr:
        print(p2a[r] - p2a[l-1])
if __name__ == '__main__':
    main()