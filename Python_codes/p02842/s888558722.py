import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

def binary_search(ok, ng, cond):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if cond(mid):
            ok = mid
        else:
            ng = mid
    return ok

candidate = binary_search(n, 0, lambda x: x * 1.08 >= n)
if n == int(candidate * 1.08):
    print(candidate)
else:
    print(':(')
