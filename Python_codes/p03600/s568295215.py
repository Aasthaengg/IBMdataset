def main():
    N = int(input())
    dist = [list(map(int, input().split())) for _ in range(N)]

    update = False
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if not (dist[i][k] and dist[k][j]): continue  # パスなし
                d = dist[i][k] + dist[k][j]
                if dist[i][j] > d:
                    dist[i][j] = d
                    update = True

    if update:
        print(-1)
        return

    ans = 0
    for j in range(N):
        for i in range(j):
            for k in range(N):
                if not (dist[i][k] and dist[k][j]): continue  # パスなし
                d = dist[i][k] + dist[k][j]
                if d == dist[i][j]: break  # divisible
            else:
                ans += dist[i][j]
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
