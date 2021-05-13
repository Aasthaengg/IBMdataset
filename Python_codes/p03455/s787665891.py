# A - Product
# https://atcoder.jp/contests/abc086/tasks/abc086_a

a, b = map(int, input().split())

result = 'Even'

if (a * b % 2) == 1:
    result = 'Odd'

print(result)
