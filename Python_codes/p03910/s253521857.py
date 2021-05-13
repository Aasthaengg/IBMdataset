N = int(input())
left = 0
right = 10 ** 7 + 1
while right - left > 1:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 < N:
        left = mid
    else:
        right = mid
ans = {i for i in range(1, right + 1)}
rem = N - right
except_n = right * (right - 1) // 2 - N + right
ans -= {except_n}
[print(i) for i in ans]
