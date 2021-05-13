X = list(map(int, input().split()))
S = sorted(X, reverse=True)
X, Y = S[0] * 10 + S[1], S[2]
print(X + Y)