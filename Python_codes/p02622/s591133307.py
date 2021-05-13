S, T = [input() for _ in range(2)]
print(sum(s != t for s, t in zip(S, T)))