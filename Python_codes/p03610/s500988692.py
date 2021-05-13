s = input()

print("".join([c for idx, c in enumerate(s) if idx % 2 == 0]))
