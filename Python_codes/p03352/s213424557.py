X = int(input())
nums = set()
nums.add(1)
for b in range(2, 40):
    p = 2
    while True:
        if b**p <= 1000:
            nums.add(b**p)
            p += 1
        else:
            break
ans = -1
for num in nums:
    if num <= X:
        ans = max(ans, num)
print(ans)
