N, M, K = map(int, input().split())
ret = False
for i in range(N+1):
    for j in range(M+1):
        r = j*N+i*M-2*i*j
        # print(i,j,r)
        if r >= K:
            break
    if r == K:
        ret = True
        # print(i,j)
        break
        
print('Yes' if ret else 'No')