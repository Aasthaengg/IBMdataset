n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = arr[n//2] - arr[n//2-1]
print(ans)