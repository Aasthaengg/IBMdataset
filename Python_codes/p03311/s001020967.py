n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = a[i] - (i + 1)
a = sorted(a)
b = a[n // 2]
total = 0
for i in range(n):
    total += abs(a[i] - b)
print(total)
