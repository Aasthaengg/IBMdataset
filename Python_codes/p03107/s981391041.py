s = input()
x = s.count("0")
print(2 * min(x, len(s) - x))