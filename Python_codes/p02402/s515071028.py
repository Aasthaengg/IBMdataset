n = int(input())
ins = input().split()
nums = [int(x) for x in ins]
print("%d %d %d" % (min(nums), max(nums), sum(nums)))