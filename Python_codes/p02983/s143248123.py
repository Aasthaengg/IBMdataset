N, K = map(int,input().split())
ans = float('inf')
for i in range(N,K):
    for j in range(i+1,K+1):
        mod = (i*j)%2019
        ans = min(mod, ans)
        if mod==0:
            break
    else:
        continue
    break
print(ans)