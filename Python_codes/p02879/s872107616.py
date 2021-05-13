# 問題: https://atcoder.jp/contests/abc144/tasks/abc144_a

a, b = map(int, input().strip().split())

if 0 < a < 10 and 0 < b < 10:
    print(a*b)
else:
    print(-1)
