n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
for i in range(n):
    if a[i] > b[i]:
        cnt1 += a[i] - b[i]
    elif a[i] < b[i]:
        cnt2 += -(-(b[i] - a[i]) // 2)
        if (b[i] - a[i]) % 2 == 1:
            cnt1 += 1
if cnt1 <= cnt2:
    print("Yes")
else:
    print("No")