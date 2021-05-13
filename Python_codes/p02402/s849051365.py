input()
nums = list(map(int, input().split()))
n1, n2, n3 = min(nums), max(nums), sum(nums)
print(' '.join(map(str, [n1, n2, n3])))