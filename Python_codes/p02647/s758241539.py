def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    Z = [N]*N

    while K > 0 and A != Z:
        K-=1
        B = [int(0)]*(N+1)
        for i in range(N):
            B[max(int(0),i-A[i])]+=1
            B[min(N-1,i+A[i])+1]-=1
        for i in range(1,N):
            B[i]+=B[i-1]

        A = B[0:N]

    print(' '.join(map(str,A)))

if __name__ == '__main__':
    main()