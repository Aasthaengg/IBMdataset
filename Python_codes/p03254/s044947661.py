n, x = map(int, input().split())

nums = sorted(list(map(int, input().split())))

count = 0
for i, num in enumerate(nums):
    if (i < n-1 and num <= x) or (i == n-1 and num == x):
        count += 1
        x -= num        
    else:
        break

print(count)