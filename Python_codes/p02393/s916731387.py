in_str = raw_input().split()
nums = []
for s in in_str:
    nums.append(int(s))
nums.sort()
for n in nums:
    print n,