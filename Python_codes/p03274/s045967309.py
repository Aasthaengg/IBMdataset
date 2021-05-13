from bisect import bisect_left

n, k = [int(i) for i in input().split()]
x_list = [int(i) for i in input().split()]

ans = 10 ** 9
i = bisect_left(x_list, 0)
for j in range(max(i - k, 0), min(i + 1, n - k + 1)):
    if j == i - k:
        temp = abs(x_list[j])
    elif j == i:
        temp = x_list[j + k - 1]
    else:
        temp = x_list[j + k - 1] - x_list[j] + min(-x_list[j], x_list[j + k - 1])
    
    if temp < ans:
        ans = temp
print(ans)