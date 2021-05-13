nums = list(map(int, input().split())) # "1 2 3"と入力

a = nums[0]
b = nums[1]

sums = a + b
diff = a - b
kakeru = a * b

ans = max(sums,diff,kakeru)

print(ans)
