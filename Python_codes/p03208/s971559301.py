N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort()
df = 0
min_h = H[K-1]-H[0]

for i in range(1, N-K+1):
    new_h = H[i+K-1]-H[i]
    if new_h < min_h:
        min_h = new_h

print(min_h)
