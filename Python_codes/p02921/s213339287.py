S = list(input())
T = list(input())

same = [s for s, t in zip(S, T) if s == t]
print(len(same))

