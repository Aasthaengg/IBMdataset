n, x = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for i in range(n-1):
    diff = (a[i] + a[i+1]) - x
    if diff <= 0:
        continue
    if diff <= a[i+1]:
        a[i+1] -= diff
    else:
        a[i] -= (diff - a[i+1])
        a[i+1] = 0
    cnt += diff
print(cnt)