n = int(input())
nums = list(map(int,input().split()))
alice = 0
bob = 0

nums.sort()
while nums:
    alice+=nums.pop()
    if nums:
        bob+=nums.pop()

print(alice-bob)