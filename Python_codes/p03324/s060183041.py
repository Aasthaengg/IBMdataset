# https://atcoder.jp/contests/abc100/tasks/abc100_b

d, n = map(int, input().split())
if d == 0:
    if n == 100:
        ans = 101
    else:
        ans = n
else:
    if n == 100:
        ans = 100 ** d * 101
    else:
        ans = 100 ** d * n
print(ans)