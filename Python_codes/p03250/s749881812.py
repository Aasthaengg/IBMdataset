x, y, z = map(int, input().split())
i = x + y + z
print(max(x, y, z)* 10 + i - max(x, y, z))
