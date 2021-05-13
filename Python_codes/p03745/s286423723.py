n = int(input())
a = list(map(int, input().split()))

ans = 1
status = 0
prev = a[0]

for i in a:
    diff = i - prev

    if diff == 0:
        pass
    elif diff > 0:
        if status >= 0:
            status = diff
        else:
            ans += 1
            status = 0
    else:
        if status <= 0:
            status = diff
        else:
            ans += 1
            status = 0

    prev = i

print(ans)