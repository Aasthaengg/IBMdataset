N, M, K = map(int, input().split())
def check():
    for i in range(M):
        P = M-2*i
        K1 = K - i*N
        if P==0:
            if K1 == 0:
                return True
            return False
        if K1%P==0 and K1//P<=N and K1//P>=0:
            return True
    return False
if check():
    print('Yes')
else:
    print('No')