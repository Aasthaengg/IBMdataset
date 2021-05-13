S = input()
T = input()
res = sum(s == t for s, t in zip(S, T))
print(res)