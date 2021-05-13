def resolve():
    K = int(input())
    print((K//2)**2 if K%2 == 0 else (K+1)//2 * (K-1)//2)
resolve()