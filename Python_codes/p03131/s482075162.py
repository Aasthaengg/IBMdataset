k, a, b = map(int, input().split())
diff = b - a
if diff <= 2:
    print(1 + k)
    exit()
times = a - 1
print(a + (k-times) // 2 * diff + (k-times) % 2)