MOD = 10**9 + 7
N = int(input())
S = input()

X = {}

for s in S:
    if not(s in X):
        X[s] = 0

    X[s] += 1

ans = 1
for v in X.values():
    ans = ans*(v+1)%MOD

print((ans-1)%MOD)
