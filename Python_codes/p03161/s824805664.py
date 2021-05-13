n, k = map(int, input().split())
h = list(map(int, input().split()))

a = [10**10] * n

a[0] = 0
for i in range(0,n):
    for x in range(1,k+1):
        j = i+x
        if j >= n:
            continue
        a[j] = min(a[j], a[i] + abs(h[i] - h[j]))

print(a[n-1])
