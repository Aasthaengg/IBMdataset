# https://atcoder.jp/contests/agc015/tasks/agc015_a

n, a, b = map(int, input().split())

if b < a:
    print(0)
elif a != b and n == 1:
    print(0)
else:
    MIN = a * (n - 1) + b
    MAX = a + (n - 1) * b
    ans = MAX - MIN + 1
    print(ans)