a, b, c = sorted(map(int, input().split()))
print((c - a) // 2 + (c - b) // 2 + (((c - a) % 2 + (c - b) % 2) ^ 3) % 3)