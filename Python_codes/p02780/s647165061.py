N, K = map(int, input().split())
p = list(map(int, input().split()))

e = (sum(p[0:K])+K) / 2
max_e = e
for i in range(1, N-K+1):
    e += -(p[i-1]+1)/2 + (p[i+K-1]+1)/2
    max_e = max(max_e, e)
    
print(max_e)