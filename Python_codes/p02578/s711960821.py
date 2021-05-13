s = int(input())
arr = list(map(int, input().split()))

ans = 0

for i in range(1,s):
    if arr[i] < arr[i-1]:
        ans += (arr[i-1]-arr[i])
        arr[i] = arr[i-1]

print(ans)   
