nums = list(map(int, input().split()))

max_num = max(nums)
sum_num = sum(nums)

if max_num * 3 % 2 != sum_num % 2:
    max_num += 1

ans = (max_num * 3 - sum_num) // 2
print(ans)
