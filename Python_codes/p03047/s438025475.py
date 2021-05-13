def solve():
    N,K = list(map(int,input().split())) 
    if K <= N:
        print(N-K+1)
    else:
        print(0)

solve()