n = int(input())
a = list(map(int, input().split()))
a.sort()
total = 0
for i in range(n, n * 3, 2):
    total += a[i]
print(total)
