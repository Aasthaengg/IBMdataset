n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= i + 1
a.sort()
b = a[n // 2]
print(sum(abs(i - b) for i in a))