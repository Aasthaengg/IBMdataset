S = input()
T = input()
print(sum([1 if s == t else 0 for s, t in zip(S, T)]))