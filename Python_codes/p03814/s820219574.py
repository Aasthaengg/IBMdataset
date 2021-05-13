s = list(input())
sr = s[::-1]
a = s.index("A")
z = sr.index("Z")
print(len(s) - z - a)

