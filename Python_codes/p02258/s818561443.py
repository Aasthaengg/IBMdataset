import sys

num_list = int(sys.stdin.readline())
lines = sys.stdin.readlines()
nums = map(int, lines)

max_diff = -sys.maxint - 1
min_val = nums.pop(0)
for num in nums :
    diff = num - min_val
    if diff > max_diff :
        max_diff = diff
    if num < min_val :
        min_val = num

print max_diff