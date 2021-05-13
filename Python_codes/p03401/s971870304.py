n = int(input())
a = list(map(int, input().split()))
b = [0] * (n + 2)
b[1] = abs(a[0])
for i in range(2, n + 1):
    b[i] = b[i - 1] + abs(a[i - 2] - a[i - 1])
b[n + 1] = abs(0 - a[n - 1]) + b[n]
a = [0] + a + [0]
for i in range(n):
    print(b[n + 1] + abs(a[i] - a[i + 2]) - abs(b[i] - b[i + 2]))