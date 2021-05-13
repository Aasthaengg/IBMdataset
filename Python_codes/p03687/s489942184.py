from collections import Counter
import sys

sys.setrecursionlimit(10 ** 6)

mod = 1000000007
inf = int(1e18)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def inverse(a):
    return pow(a, mod - 2, mod)


def usearch(x, a):
    lft = 0
    rgt = len(a) + 1
    while rgt - lft > 1:
        mid = (rgt + lft) // 2
        if a[mid] <= x:
            lft = mid
        else:
            rgt = mid
    return lft

def solve(a, s):
    b = []
    for i in range(len(s)):
        if s[i] == a:
            b.append(i)
    if len(b) == 0:
        return len(s) - 1
    ans = 0
    for i in range(len(b)-1):
        ans = max(ans, (b[i+1] - b[i] - 1))
    ans = max(ans, b[0])
    ans = max(ans, len(s) - b[-1] - 1)
    return ans

def main():
    s = input()
    ans = len(s)
    for i in range(26):
        ans = min(ans, solve(chr(ord('a') + i), s))
    print(ans)
main()