N, K = map(int, input().split())
h = list(map(int, input().split()))
 
S = [0] * N
S[0] = 0
 
for i in range(1, N):
    value = S[i - 1] + abs(h[i] - h[i - 1])
    maxStep = min(K, i)
    for step in range(1, maxStep + 1):
        value = min(value, S[i - step] + abs(h[i] - h[i - step]))
    S[i] = value
print(S[N - 1])