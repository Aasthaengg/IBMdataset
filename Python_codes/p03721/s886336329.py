n, k = map(int,input().split())

nums = [0]*(10**5+1)

for i in range(n):
    a, b = map(int,input().split())
    nums[a] += b
    
now = 0
for i,n in enumerate(nums):
    now += n
    if now >= k:
        print(i)
        break