n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

dp = [1] * (k+1)


for i in range(1, k+1):
    curr = 1
    for j in range(len(arr)):
        if arr[j] <= i:
            if dp[i-arr[j]] == 0:
                curr = 1
            else:
                curr = 0
                break
    
    dp[i] = curr

# print(dp)

if dp[-1] == 1:
    print("Second")
else:
    print("First")