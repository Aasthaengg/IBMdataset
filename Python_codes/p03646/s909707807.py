K = int(input())

def construct(K, N=50):
    As = [N+(K//N-1)-K%N]*50 # 50+K//50 - K%50
    q = K%N
    for q_ in range(q): As[q_] = N+K//N
    print(N)
    print(' '.join(map(str, As)))
    
construct(K)