n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if ans == 0:
        ans = 0
    if a[i] == ans + 1:
        ans += 1
if ans == 0:
    print(-1)
else:
    print(n - ans)
