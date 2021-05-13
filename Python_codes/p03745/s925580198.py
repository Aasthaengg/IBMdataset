# AGC 013 A - Sorted Arrays

n = int(input())
a = list(map(int, input().split()))
up, down = 0, 0
ans = 0

for i in range(1, n):
    if a[i] > a[i-1]:
        up += 1
    if a[i-1] > a[i]:
        down += 1
    if up * down > 0:
        ans += 1
        up = 0
        down = 0
print(ans + 1)