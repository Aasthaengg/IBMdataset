S = input()
T = input()

print(sum([c1 != c2 for c1, c2 in zip(S, T)]))
