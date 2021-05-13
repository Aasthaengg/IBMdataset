import sys
input = sys.stdin.readline

N,K = list(map(int,input().split()))
H = sorted([int(input()) for _ in range(N)])
ans = float('inf')
for i in range(N-K+1):
    ans = min(H[i+K-1] - H[i],ans)
print(ans)
