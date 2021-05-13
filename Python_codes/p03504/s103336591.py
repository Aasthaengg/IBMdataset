N, C = map(int, input().split())
X = [[] for _ in range(C)]
A = []
for _ in range(N):
    s, t, c = map(int, input().split())
    A.append((s, t, c-1))

A = sorted(A)
for s, t, c in A:
    if X[c] and X[c][-1][1] == s:
        X[c][-1][1] = t
    else:
        X[c].append([s-1, t])
Y = []
for x in X:
    Y += x
Z = [0] * 101010
for s, t in Y:
    Z[s+1] += 1
    Z[t+1] -= 1

for i in range(1, 101010):
    Z[i] += Z[i-1]

print(max(Z))
