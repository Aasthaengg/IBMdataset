import sys

sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline

######################################################

s = input().split('T')
x, y = [int(_) for _ in input().split()]


def m(dp, first_idx):
    for i in range(first_idx, len(s), 2):
        step = len(s[i])

        next_dp = set()
        for item in dp:
            next_dp.add(item + step)
            next_dp.add(item - step)
        dp = next_dp

    return dp


if len(s) > 0:
    xs = {len(s[0])}
    xs = m(xs, 2)
else:
    xs = {0}
if len(s) > 1:
    ys = m({0}, 1)
else:
    ys = {0}

if x in xs and y in ys:
    print('Yes')
else:
    print('No')
