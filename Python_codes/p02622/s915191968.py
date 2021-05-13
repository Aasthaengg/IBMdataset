S = input()
T = input()
assert len(S) == len(T)
print(len([(s,t) for s,t in zip(S,T) if s != t]))