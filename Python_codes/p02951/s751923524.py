# A - Transfer
# https://atcoder.jp/contests/abc136/tasks/abc136_a

A, B, C = map(int, input().split())

result = C - (A - B)

if result < 0:
    result = 0

print(result)
