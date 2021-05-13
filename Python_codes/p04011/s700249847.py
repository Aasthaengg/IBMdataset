N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if N<=K:
    ans = X*N
else:
    ans = X*K
    ans += Y*(N-K)
print(ans)