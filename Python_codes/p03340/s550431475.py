import itertools

n = int(input())
ls = [0] + list(map(int, input().split()))
s0 = list(itertools.accumulate(ls))
s1 = list(itertools.accumulate(ls, lambda a, b: a ^ b))
res = 0
left = 0
right = 1
count = 0
while left <= n:
    while left < right - 1:
        a = s0[right] - s0[left]
        b = s1[right] ^ s1[left]
        if a != b:
            left += 1
        else:
            res -= (right - left - 1) * (right - left) // 2
            break
    while right <= n + 1:
        if right == n + 1:
            break
        a = s0[right] - s0[left]
        b = s1[right] ^ s1[left]
        if a == b:
            right += 1
        else:
            break
    res += (right - left - 1) * (right - left) // 2
    if right == n + 1:
        break
print(res)