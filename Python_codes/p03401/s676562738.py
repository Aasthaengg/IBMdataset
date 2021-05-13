N = int(input())
arr = [0] + list(map(int, input().split())) + [0]
ans = 0
for i in range(1,len(arr)):
    ans += abs(arr[i]-arr[i-1])
for i in range(1,len(arr)-1):
    print(ans-abs(arr[i-1]-arr[i])-abs(arr[i+1]-arr[i])+abs(arr[i-1]-arr[i+1]))