N,M,K = map(int, input().split())
for i in range(N+1):
    b = i * M
    for j in range(M+1):
        b -= i
        b += N-i
        if b == K:
            print('Yes')
            exit()
print('No')
