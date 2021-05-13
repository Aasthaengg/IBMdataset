from sys import maxsize

n = int(input())
a = list(map(int, input().split()))

res = maxsize
for i in (0, 1):
    cumsum = cnt = 0
    for k in range(n):
        if k % 2 == i:
            if cumsum + a[k] <= 0:
                cnt += abs(1 - (cumsum + a[k]))
                cumsum = 1
            else:
                cumsum += a[k]
        else:
            if cumsum + a[k] >= 0:
                cnt += abs(-1 - (cumsum + a[k]))
                cumsum = -1
            else:
                cumsum += a[k]
    if cnt < res:
        res = cnt

print(res)
