n, m, K = map(int, input().split())

ans = 'No'
for k in range(n + 1):
    for l in range(m + 1):
        if k * (m - l) + l * (n - k) == K:
            ans = 'Yes'
            
print(ans)
