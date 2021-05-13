n = int(input())
a = list(map(int, input().split()))
total = sum(a)
total_a, total_b = 0, 0
i = 0
while total_a + a[i] <= total / 2:
    total_a += a[i]
    i += 1
i = n - 1
while total_b + a[i] <=  total / 2:
    total_b += a[i]
    i -= 1

print(total - max(total_a, total_b) * 2)