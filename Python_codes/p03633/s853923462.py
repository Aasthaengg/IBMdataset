import fractions
N = int(input())
T = []
for i in range(N):
    T.append(int(input()))
X = T[0]
for i in range(1, N):
    X = X*T[i] // fractions.gcd(X, T[i])
print(X)