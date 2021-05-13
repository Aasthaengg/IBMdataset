N, K = map(int, input().split())

def solve():
    if K>(N-1)*(N-2)//2:
        print(-1)
        return
    M = (N-1)*N//2-K
    print(M)
    for i in range(1,N):
        print(i,N)
    edge = N-1
    if edge==M:
        return
    for i in range(1,N-1):
        for j in range(i+1,N):
            print(i,j)
            edge += 1
            if edge==M:
                return
solve()