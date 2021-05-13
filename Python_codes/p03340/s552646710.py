import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]

right = 0
s = 0
ans = 0

for left in range(n):
    while right < n and s ^ a[right] == s | a[right]:
        s ^= a[right]
        right += 1
    
    ans += right - left

    if left == right:
        right += 1
    else:
        s -= a[left]

print(ans)