# APC001A - Two Integers
x, y = list(map(int, input().rstrip().split()))
print(x if x % y else -1)