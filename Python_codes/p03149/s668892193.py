nums = list(map(int, input().split()))
nums.sort()

ans = [1, 4, 7, 9]

print('YES' if nums == ans else 'NO')