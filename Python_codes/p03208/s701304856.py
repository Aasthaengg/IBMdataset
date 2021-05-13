N, K = list(map(int, input().split()))
h = [0]
for _ in range(N):
    h += [int(input())]        
h = sorted(h)

min_value = h[-1]
for i in range(K, N + 1):
    min_value = min(h[i] - h[i - K + 1], min_value)
print(min_value)