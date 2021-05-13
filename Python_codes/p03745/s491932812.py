n = int(input())
a = list(map(int, input().split()))

trend = 0
cnt = 0
for i in range(1,n):
    if trend == 0:
        if a[i-1] == a[i]:
            pass
        elif a[i-1] < a[i]:
            trend = 1
        else:
            trend = -1
    elif trend == 1:
        if a[i-1] > a[i]:
            trend = 0
            cnt += 1
        else:
            pass
    else:
        if a[i-1] < a[i]:
            trend = 0
            cnt += 1
        else:
            pass

print(cnt+1)

