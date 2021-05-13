# https://atcoder.jp/contests/abc112/tasks/abc112_d

n, m = map(int, input().split())
if n == 1:
    ans = m
else:
    ans = 1
    i = 1
    limit = m / n
    while i <= limit:
        if m % i == 0 and m // i >= n:
            ans = max(ans, i)
        i += 1
print(ans)
