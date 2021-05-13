n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dm = 0
for i in range(n):
    dm += min(a[i], b[i])
    b[i] = b[i] - a[i]
    if b[i] > 0:
        dm += min(b[i], a[i + 1])
        a[i + 1] = max(a[i + 1] - b[i], 0)
print(dm)