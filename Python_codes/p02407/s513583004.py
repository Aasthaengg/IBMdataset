n = input()
nums = map(int, raw_input().split(" "))
nums.reverse()
result = map(str,nums)
print " ".join(result)