N = int(input())
a = list(map(int, input().split()))
up = -1
ans = 1
for i in range(1, N):
    if up == 0 and a[i] - a[i-1] > 0:
        up = -1
        ans += 1
    elif up == 1 and a[i] - a[i-1] < 0:
        up = -1
        ans += 1
    elif up == -1 and a[i] - a[i-1] > 0:
        up = 1
    elif up == -1 and a[i] - a[i-1] < 0:
        up = 0
print(ans)