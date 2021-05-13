n = int(input())
a = list(map(int, input().split()))
left = 0
right = 0

ans = 0
now = 0
while True:
    while right < n and now + a[right] == now ^ a[right]:
        now += a[right]
        right += 1

    if left >= n:
        break

    ans += right - left
    now -= a[left]
    left += 1

print(ans)
