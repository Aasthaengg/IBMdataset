am = int(input())
arr = list(map(int,input().split()))
if am == 1:
    print(0)
else:
    dp = [0,abs(arr[1]-arr[0])]
for i in range(2,am):
    dp.append(min(dp[i-2] + abs(arr[i]-arr[i-2]), dp[i-1] + abs(arr[i]-arr[i-1])))
print(dp[-1])