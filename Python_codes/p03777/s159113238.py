a, b = map(lambda c: c == "H", input().split())
print("D" if a ^ b else "H")