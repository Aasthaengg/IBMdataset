n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(k):
    c += a[i]
for i in range(k, n):
    d = c - a[i - k] + a[i]
    if d > c:
        print("Yes")
    else:
        print("No")
    c = d