N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]

h.sort()
result = 10**9+1
for i in range(N-K+1):
    a = abs(h[i] - h[i+K-1])
    if a < result:
        result = a

print(result)