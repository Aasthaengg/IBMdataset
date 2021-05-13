n = input()[2:]
a, b = set(n[:2]), set(n[2:])
print("Yes" if len(a) == len(b) == 1 else "No")