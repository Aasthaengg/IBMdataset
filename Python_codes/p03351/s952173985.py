# A - Colorful Transceivers
# https://atcoder.jp/contests/abc097/tasks/abc097_a

a, b, c, d = map(int, input().split())

result = 'No'

if abs(a - c) <= d:
    result = 'Yes'
elif abs(a - b) <= d and abs(b - c) <= d:
    result = 'Yes'

print(result)
