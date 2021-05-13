from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
a.sort()
total = [0] * n
total[0] = a[0]
for i in range(1, n):
    total[i] = a[i] + total[i - 1]
ans = 1
for i in range(n - 1, 0, -1):
    if a[i] <= total[i - 1] * 2:
        ans += 1
    else:
        break

print(ans)