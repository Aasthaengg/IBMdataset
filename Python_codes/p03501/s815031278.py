# A - Parking
# https://atcoder.jp/contests/abc080/tasks/abc080_a

n, a, b = map(int, input().split())

plan = [n * a, b]
print(min(plan))
