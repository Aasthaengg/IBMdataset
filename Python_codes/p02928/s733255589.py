n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
l = []
for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            cnt += (k + 1) * k // 2 if j > i else k * (k - 1) // 2
print(cnt % 1000000007)