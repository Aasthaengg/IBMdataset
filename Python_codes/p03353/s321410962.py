S, k = open(0).read().split()
k = int(k)
x = set(sorted(S)[:min(k, len(S))])
A = set()
for i, c in enumerate(S):
    if c in x:
        s = ''
        for j in range(i, min(i+k, len(S))):
            s += S[j]
            A.add(s)
print(sorted(A)[k-1])