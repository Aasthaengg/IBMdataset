
N, M, K = map(int, input().split())

def main(N, M, K):
    for i in range(0, N+1):
        for j in range(0, M+1):
            if i * (M - j) + j * (N - i) == K:
                return True
    return False

res = main(N, M, K)

if res == True:
    print('Yes')
else:
    print('No')



