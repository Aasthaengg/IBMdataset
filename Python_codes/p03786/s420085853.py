n = int(input())
a = list(map(int, input().split()))
a.sort()
cum_a = [a[0]]
for i in range(1, n):
    cum_a.append(cum_a[i-1]+a[i])
res = 0
for i in range(1, n):
    if cum_a[i-1]*2 < a[i]:
        res = i

print(n-res)