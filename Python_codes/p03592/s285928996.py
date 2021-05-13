N, M, K = map(int, input().split())

isok = False
for x in range(N+1):
    for y in range(M+1):
        if x*(M-y)+y*(N-x) == K:
            isok = True
            break

print('Yes' if isok else 'No')