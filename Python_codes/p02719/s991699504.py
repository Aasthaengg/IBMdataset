import sys
input = sys.stdin.readline

def binary_search_int(ok, ng, solve):
    """
    :param ok: solve(x) = True を必ず満たす点
    :param ng: solve(x) = False を必ず満たす点
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok, ng

##############################################################

def solve(x):
    """ ある点 x を境にして True と False が二分されるような関数"""
    return N - K*x >= 0

N, K = map(int, input().split())

a, b = binary_search_int(0, 10**18, solve)
print(min(abs(N-a*K), abs(N-b*K)))
