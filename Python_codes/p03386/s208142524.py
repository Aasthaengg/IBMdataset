a,b,k = map(int, input().split())

nums = []
for i in range(a, min(b+1,a+k)): nums.append(i)
for i in range(b, max(a-1,b-k), -1): nums.append(i)
for i in sorted(set(nums)): print(i)