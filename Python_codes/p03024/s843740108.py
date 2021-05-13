s = input()
print("YES" if 15 - len(s) + s.count("o") >= 8 else "NO")