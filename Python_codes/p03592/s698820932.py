N, M, K = map(int, input().split())

for r in range(N+1):
    for c in range(M+1):
        black = (M*r)+(N*c)-(r*c*2)
        if black == K:
            print('Yes')
            exit(0)
print('No')
