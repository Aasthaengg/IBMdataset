# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(N, Hs):
    ans = 0
    tmp = 0
    for i in range(N - 1):
        if Hs[i] >= Hs[i + 1]:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    Hs = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, Hs)
