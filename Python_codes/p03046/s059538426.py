def main():
    import sys
    input = sys.stdin.readline
    M, K = map(int, input().split())
    answer = []
    if M==K==1:
        print(-1)
    elif 2**M - 1 < K:
        print(-1)
    elif K == 0:
        for i in range(2**M):
            answer += [i,i]
    else:
        for i in range(K):
            answer += [i]
        for i in range(K+1,2**M):
            answer += [i]
        answer += [K]
        for i in range(1,2**M-K):
            j = 2**M - i
            answer += [j]
        for i in range(2**M-K+1,2**M+1):
            j = 2**M - i
            answer += [j]
        answer += [K]
    print(*answer)
    
    
main()