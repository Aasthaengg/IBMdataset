n = int(input())
a = [int(_) for _ in input().split()]

avg = sum(a) / n

idx = 0
val = float('INF')
for i in range(n):
    if abs(a[i]-avg) < val:
        idx = i
        val = abs(a[i]-avg)
print(idx)