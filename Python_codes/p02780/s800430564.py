import copy

n, k = map(int, input().split())
p = list(map(int, input().split()))

s = sum(p[:k])
smax = copy.deepcopy(s)
for i in range(n-k):
    s += p[i+k] - p[i]
    smax = max(smax, s)

print((smax+k)/2)
