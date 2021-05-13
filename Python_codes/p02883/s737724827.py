n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse=True)
time = []
for i in range(n):
    time.append(a[i]*f[i])

left = -1
right = 10**12 + 1
while right - left > 1:
    mid = (left + right)//2
    count = 0
    flag = True
    for i in range(n):
        if time[i] <= mid:
            continue
        sa = time[i] - mid
        if sa % f[i] == 0:
            count += sa // f[i]
        else:
            count += sa // f[i] + 1
        if count > k:
            flag = False
            break
    if flag:
        right = mid
    else:
        left = mid
print(right)