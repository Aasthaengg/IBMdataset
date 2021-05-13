S = input()
T = input()
counts = []
for i in range(len(S) - len(T)+1):
  count = len([s for s,t in zip(S[i:],T) if s != t])
  counts.append(count)
print(min(counts))