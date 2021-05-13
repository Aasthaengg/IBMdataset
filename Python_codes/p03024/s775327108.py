s = input()
a, b = s.count("o"), s.count("x")
print("YES" if a+15-a-b>=8 else "NO")