N,K = list(map(int,input().split()))
h = []
for i in range(N):
    h.append(int(input()))
sorted_h = sorted(h)
minDelta = 10 ** 10
for i in range(N-K+1):
    delta = sorted_h[i+K-1] - sorted_h[i]
    if minDelta > delta:
        minDelta = delta
print(minDelta)