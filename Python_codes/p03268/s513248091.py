from collections import Counter
n, k = map(int, input().split())
ans = 0
mod = Counter([i%k for i in range(1,n+1)])
for a in range(k):
    b = (k-a)%k
    if 2*b%k !=0: continue
    ans += mod[a]*mod[b]*mod[b]
print(ans)