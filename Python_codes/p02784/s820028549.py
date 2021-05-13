h, n = map(int, input().split())
a = list(map(int, input().split()))
x = 0
for i in range(n):
    x = x + a[i]
print("Yes" if x >= h else "No")