N, K= map(int, input().split())

h = list(sorted([int(input()) for i in range(N)]))
h_dif = [h[i+K-1] - h[i] for i in range(N-K+1)]
print(min(h_dif))