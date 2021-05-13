import sys

n, k = map(int, input().split())

max_num = n // k
min_num = max_num if n % k == 0 else max_num - 1

print(max_num-min_num)
