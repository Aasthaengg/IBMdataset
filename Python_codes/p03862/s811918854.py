n, x = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = sum(arr)

for i in range(n - 1):
    if arr[i] + arr[i + 1] > x:
        arr[i + 1] -= min(arr[i] + arr[i + 1] - x, arr[i + 1])
    if arr[i] + arr[i + 1] > x:
        arr[i] -= arr[i] - x

print(sum_arr - sum(arr))