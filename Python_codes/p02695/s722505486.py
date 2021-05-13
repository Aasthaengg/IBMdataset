import sys
sys.setrecursionlimit(100000)
input = sys.stdin.buffer.readline

n, m, q = [int(i) for i in input().strip().split()]
abcd = []
canditates = []
ans = 0


for _ in range(q):
    abcd.append([int(i) for i in input().strip().split()])


def helper(_min, _max, cur, res):
    if res == 0:
        canditates.append(list(cur))
    else:
        for i in range(_min, _max):
            cur.append(i)
            helper(i, _max, cur, res - 1)
            cur.pop()


helper(1, m + 1, [], n)

for A in canditates:
    _temp = 0
    for a, b, c, d in abcd:
        if A[b - 1] - A[a - 1] == c:
            _temp += d

    ans = max(ans, _temp)

print(ans)
