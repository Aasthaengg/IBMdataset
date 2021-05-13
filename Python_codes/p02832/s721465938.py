n = int(input())
a = [int(x) - 1 for x in input().split()]

target, point = 0, 0
ans = 0
for i in range(n):
    if a[i] == target:
        ans += i - point
        point = i + 1
        target += 1

if target == 0:
    print(-1)
else:
    ans += n - point
    print(ans)