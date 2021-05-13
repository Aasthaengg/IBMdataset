N, K, *h = map(int, open(0).read().split())

h_sort = sorted(h)

ans = 10**9

for i in range(N-K+1):
    ans = min(ans, h_sort[i+K-1] - h_sort[i])
    
print(ans)