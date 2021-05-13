n, m = list(map(int, input().split()))
coin = list(map(int, input().split()))
a = [i for i in range(n + 1)]
for j in coin:
    for i in range(j, n + 1):
        a[i] = min(a[i], a[i - j] + 1)

print(a[n])

