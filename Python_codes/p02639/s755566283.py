import sys
line = sys.stdin.readlines()[0].rstrip("\n")
nums = line.split(" ")
print(nums.index("0") + 1)
