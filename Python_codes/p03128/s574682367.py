import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split())
a = list(map(int, input().split()))
memo = {}
matches = [100, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def doit(n):
    if n == 0:
        return ""
    if not n in memo:
        ret = None
        for d in a:
            m = matches[d]
            if n - m >= 0 and doit(n - m) is not None:
                r = max(doit(n - m) + str(d), str(d) + doit(n - m))
                if ret is None or len(r) > len(ret) or len(r) == len(ret) and r > ret:
                    ret = r
        memo[n] = ret
    return memo[n]

print(doit(n))