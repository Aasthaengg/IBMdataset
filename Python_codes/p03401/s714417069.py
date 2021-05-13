n = int(input())
a = [0] * (n + 2)
A = list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] = A[i - 1]
d = [abs(a[i + 1] - a[i]) for i in range(n + 1)]
s = sum(d)
print(s - d[0] - d[1] + abs(a[2]))
for i in range(2, n):
    print(s - d[i - 1] - d[i] + abs(a[i + 1] - a[i - 1]))
print(s - d[-1] - d[-2] + abs(a[-3]))