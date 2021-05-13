n = int(input())
ls = list(map(int, input().split()))
res = 0
left = 0
right = 0
s0 = 0
s1 = 0
while left < n:
    while right < n and s0 + ls[right] == s1 ^ ls[right]:
        s0 += ls[right]
        s1 ^= ls[right]
        right += 1
    res += right - left
    s0 -= ls[left]
    s1 ^= ls[left]
    left += 1
print(res)