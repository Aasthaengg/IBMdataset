N, K = map(int, input().split())
H = sorted([int(input()) for _ in range(N)])[::-1]
print(min([H[i]-H[i+K-1] for i in range(N-K+1)]))
