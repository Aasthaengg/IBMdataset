num = input()
nums = list(map(int, input().split()))
print("{0} {1} {2}".format(min(nums), max(nums), sum(nums)))