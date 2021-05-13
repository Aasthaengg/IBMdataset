from itertools import accumulate
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    Sss = [input().rstrip() for _ in range(N)]

    numL = numR = 0
    Pluss, Evens, Minuss = [], [], []
    for Ss in Sss:
        nums = [0] + [1 if S == '(' else -1 for S in Ss]
        nums = list(accumulate(nums))
        x = min(nums)
        y = nums[-1] - x
        x, y = abs(x), abs(y)
        if x == 0:
            numL += y
        elif y == 0:
            numR += x
        else:
            if x > y:
                Minuss.append((x, y))
            elif x < y:
                Pluss.append((x, y))
            else:
                Evens.append((x, y))

    Pluss.sort(key=lambda x: x[0])
    Minuss.sort(key=lambda x: x[1], reverse=True)

    v = numL
    for x, y in Pluss:
        v -= x
        if v < 0:
            return False
        v += y
    for x, y in Evens:
        v -= x
        if v < 0:
            return False
        v += y
    for x, y in Minuss:
        v -= x
        if v < 0:
            return False
        v += y
    v -= numR
    return v == 0


if solve():
    print('Yes')
else:
    print('No')
