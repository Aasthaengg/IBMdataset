x = int(input())
q, mod = divmod(x, 11)
print(q * 2 + (mod + 6 - 1) // 6)