import sys

n = input()
minv = input()
maxv = - 1000000000
nums = map(int, sys.stdin.readlines())
for num in nums:
    maxv = num - minv if num - minv > maxv else maxv
    minv = num if num < minv else minv

print maxv