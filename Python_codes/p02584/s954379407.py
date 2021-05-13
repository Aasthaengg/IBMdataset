# C - Walking Takahashi

X, K, D = map(int, input().split())
X = abs(X)
d = X // D
m = X % D

if K <= d:
    ans = X - (D * K)
elif (K - d) % 2 == 0:
    ans = X - (D * d)
else:
    ans = X - (D * (d+1))
print(abs(ans))