def main():
    N, K = map(int, input().split())
    *x, = map(int, input().split())

    ans = 3 * 10 ** 8
    for left, right in zip(x, x[K - 1:]):
        if left * right < 0:
            ans = min(ans, right - left + min(-left, right))
        else:
            ans = min(ans, -left if left < 0 else right)
    print(ans)


if __name__ == '__main__':
    main()

# import sys
# input = sys.stdin.readline
# 
# sys.setrecursionlimit(10 ** 7)
# 
# (int(x)-1 for x in input().split())
# rstrip()
#
# def binary_search(*, ok, ng, func):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if func(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok
