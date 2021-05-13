n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    cnt1 = 0
    cnt2 = 0

    for j in range(i):
        if a[i] > a[j]:
            cnt2 += 1

    for j in range(i+1, n):
        if a[i] > a[j]:
            cnt1 += 1
            cnt2 += 1

    cnt += cnt1*k + (k-1)*k//2*cnt2

print(cnt % 1000000007)