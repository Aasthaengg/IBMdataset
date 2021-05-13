x, y, z = map(int, input().split())
i = x + y + z
mid = i-min(x, y, z)-max(x, y, z)
print(mid - min(x, y, z) + max(x, y, z)-mid)
