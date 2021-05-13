N, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(N-1):
    if arr[i] + arr[i+1] >= x:
        tmp = arr[i] + arr[i+1] - x
        if arr[i+1] >= tmp:
            arr[i+1] -= tmp
        else:
            arr[i+1] = 0
        ans += tmp
print(ans)