import sys

n = int(raw_input())

min_R = int(raw_input())
nums = map(int, sys.stdin.readlines())

ans = -10**9

for num in nums:
    if num - min_R > ans:
        ans = num - min_R
    if num < min_R:
        min_R = num
        
print ans