n, x = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n-1):
    if a[i] + a[i+1] <= x:
        continue

    candy = a[i] + a[i+1] - x
    res += candy
    a[i+1] = max(0, a[i+1] - candy)

print(res)