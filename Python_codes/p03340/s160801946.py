n = int(input())
a = list(map(int, input().split()))

ans = 0
xor1 = a[0]
sum1 = a[0]
right = 1

for left in range(n):
    while right < n and (a[right] + sum1 == a[right] ^ xor1):
        sum1 += a[right]
        xor1 ^= a[right]
        right += 1
    ans += right - left
    if right == left: right += 1
    else:
        sum1 -= a[left]
        xor1 = xor1 ^ a[left]

print(ans)