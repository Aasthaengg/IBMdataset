n = int(input(''))
s = input('')
nums = [int(a) for a in s.split()]
print("{0} {1} {2}".format(str(min(nums)), str(max(nums)), str(sum(nums))))