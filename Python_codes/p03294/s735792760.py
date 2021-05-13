N = int(input())
nums = list(map(int, input().split()))

ans = sum(nums) - N

print(ans)