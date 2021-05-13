S = input()

A = S.index("A")
Z = len(S) - S[::-1].index("Z")

print(Z-A)
