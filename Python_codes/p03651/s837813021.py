def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if A[-1] < K:
        print('IMPOSSIBLE')
        return
    from fractions import gcd
    g = A[0]
    for i in range(1,N):
        g = gcd(g,A[i])
    if K % g == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
main()