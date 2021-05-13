N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort()
minim = 1e10
for i in range(N-K+1):
    minim = min(minim, H[i+K-1] - H[i])
print(minim)