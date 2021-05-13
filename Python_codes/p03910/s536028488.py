N = int(input())
left = 0
right = 4472
while right - left > 1:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 < N:
        left = mid
    else:
        right = mid
ans = {i for i in range(1, right + 1)}
ans -= {right * (right - 1) // 2 - N + right}
print('\n'.join(map(str, ans)))
