import sys

data = sys.stdin.readline().strip().split(' ')
nums = [int(i) for i in data]
nums.sort()
print(' '.join([str(i) for i in nums]))