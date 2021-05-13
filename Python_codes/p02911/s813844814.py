# 問題：https://atcoder.jp/contests/abc141/tasks/abc141_c


n, k, q = map(int, input().strip().split())

points = [0 for _ in range(n)]
for i in range(q):
    a = int(input())
    points[a-1] += 1
for i in range(n):
    if k - q + points[i] > 0:
        print('Yes')
    else:
        print('No')