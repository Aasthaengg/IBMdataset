K,T = list(map(int,input().split(" ")))
nums = list(map(int,input().split(" ")))
ma = max(nums)
s  = sum(nums) - ma
ans = ma  - 1
ans = max(0,ans -s )
print(ans)