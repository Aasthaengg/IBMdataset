def check():
    N,K = map(int, input().split())
    total = 0
    
    if K == 0: return N**2
    
    for b in range(1,N+1):
        if b <= K:
            continue
        
        amari = N-b*(N//b)        
        test = amari-K+1 if amari >= K else 0           
        total += (b - K) * (N//b) + test
    return total
print(check())