n = int(input())

nums = list(map(int, input().split()))

ans = (2, 2)

for div in reversed(nums):
    lower = (ans[0] + div - 1) // div * div
    upper = ans[1] // div * div
    if not lower <= upper:
        print(-1)
        exit()
    
    ans = (lower, upper + div - 1)

print(f'{ans[0]} {ans[1]}')
