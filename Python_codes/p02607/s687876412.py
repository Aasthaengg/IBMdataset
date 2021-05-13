N = int(input())
nums = list(map(int, input().split()))

cnt = 0

for i in range(N):
    num = i + 1
    
    if (num % 2 == 1 and nums[i] % 2 == 1):
        cnt += 1
        

print(cnt)
