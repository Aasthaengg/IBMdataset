# A - Libra
# https://atcoder.jp/contests/abc083/tasks/abc083_a

A, B, C, D = map(int, input().split())

ab = A + B
cd = C + D
result = 'Balanced'

if ab > cd:
    result = 'Left'
elif ab < cd:
    result = 'Right'

print(result)
