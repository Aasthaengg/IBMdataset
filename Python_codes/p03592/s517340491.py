def main():
    N,M,K = map(int,input().split())
    if K == 0 or K == N*M:
        return ('Yes')
    ans_dict = {}
    ans_dict[K] = False
    for i in range(N):
        for j in range(M+1):
            ans_dict[i*M + (N-i-i)*j] = True
    if ans_dict[K] == True:
        return('Yes')
    else:
        return('No')

print(main())
