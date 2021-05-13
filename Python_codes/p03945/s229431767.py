S = input()

print(len([0 for c1, c2 in zip(S[:-1], S[1:]) if c1 != c2]))
