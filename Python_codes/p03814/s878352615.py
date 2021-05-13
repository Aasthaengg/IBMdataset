s = list(input())

A = s.index("A")

S = list(reversed(s))
Z = S.index("Z")

print(len(s) - Z - A)
