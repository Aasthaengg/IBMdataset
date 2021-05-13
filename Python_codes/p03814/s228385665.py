s = input()
a = s.index("A")
t = [i for i, x in enumerate(s) if x == "Z"]
b = t[-1]
print(b - a + 1)