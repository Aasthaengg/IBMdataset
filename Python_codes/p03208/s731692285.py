N,K = list(map(int,input().split()))
H = sorted([int(input()) for _ in range(N)])
MIN = float('inf')
for i in range(N-K+1):
    MIN = min(MIN,H[i+K-1] - H[i])
print(MIN)