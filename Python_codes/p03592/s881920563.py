H, W, K = map(int, input().split())
for n in range(W+1):
    if W == n+n:
        continue
    l = (K-H*n)//(W-2*n)
    if 0 <= l <= H and H*n+(W-2*n)*l == K:
        print('Yes')
        exit()
print('No')
