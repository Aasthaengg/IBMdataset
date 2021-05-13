N = int(input())
K = int(input())
X = int(input())
Y = int(input())

kx = min(N, K)
ky = max(N, K) - K
print(X*kx + Y*ky)
