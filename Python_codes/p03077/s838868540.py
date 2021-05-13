# https://atcoder.jp/contests/abc123/tasks/abc123_c

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


MIN = min([a, b, c, d, e])
if n % MIN == 0:
    ans = 5 + n // MIN - 1
else:
    ans = 5 + n // MIN
print(ans)