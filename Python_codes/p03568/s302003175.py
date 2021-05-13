n = int(input())
a = list(map(int, input().split()))
ans = 0

def judge(i, nums):
    global ans
    if i == n:
        m = 1
        for j in range(n):
            m *= nums[j]
        
        if m % 2 == 0:
            ans += 1
    else:
        nums[i] = a[i] - 1
        judge(i + 1, nums)
        nums[i] = a[i]
        judge(i + 1, nums)
        nums[i] = a[i] + 1
        judge(i + 1, nums)
        
nums = [0] * n
judge(0, nums)
print(ans)