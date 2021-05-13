n, k = map(int, input().split())
h = [int(input()) for i in range(n)]

h.sort()
inf = float('inf')
min_ = inf

for i in range(n - k + 1):
    min_ = min(min_, h[i+k-1] - h[i])
print(min_)