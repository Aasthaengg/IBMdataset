a = [int(input()) for _ in range(3)]
print((a[2] + max(a[0], a[1]) - 1) // max(a[0], a[1]))