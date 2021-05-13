def resolve():
    N, K = list(map(int, input().split()))
    S = list(input())
    base = 0
    prev = S[0]
    for i in range(1, N):
        if prev == S[i]:
            base += 1
        prev = S[i]
    
    print(min(base+2*K, N-1))


if '__main__' == __name__:
    resolve()
