n = int(input())
a = [int(x) for x in input().split()]

status = 0
ans = 1
for i in range(1, n):
    if status == 0:
        if a[i-1] < a[i]:
            status = 1
        elif a[i-1] > a[i]:
            status = 2
    elif status == 1:
        if a[i-1] > a[i]:
            ans += 1
            status = 0
    elif status == 2:
        if a[i-1] < a[i]:
            ans += 1
            status = 0
print(ans)
