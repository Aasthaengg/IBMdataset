N, K = list(map(int,input().rstrip().split()))
ans = 0
for i in range(1,N+1):
    p = 1/N
    if i<K:
        while i<K:
            i *= 2
            p *= 0.5
    ans += p
print(ans)