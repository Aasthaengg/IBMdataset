n = int(input())
diff_min = pow(10, 12)
for a in range(1, n + 1):
    if n % a == 0:
        b = n // a
        diff = a + b - 2
        diff_min = min(diff_min, diff)
    if a * a > n:
        break
print(diff_min)