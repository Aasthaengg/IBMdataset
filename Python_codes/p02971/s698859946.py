import sys

input = sys.stdin.readline
max_a = 0
big_a = 0
max_index = 0
n = int(input())
for i in range(n):
    a = int(input())
    if max_a < a:
        max_index = i
        big_a = max_a
        max_a = a
    elif max_a == a:
        max_index = -1
    elif big_a < a:
        big_a = a
    else:
        continue

for i in range(n):
    print([max_a, big_a][i == max_index])