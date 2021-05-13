def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    A.sort()
    # First cond: all 0
    if A[-1] == 0:
        print('Yes')
        return
    # Second cond: N//3 -> 0, 2N//3 -> x
    if N % 3 == 0:
        if A[(2*N//3)-1] == 0 and A[-(N//3)] == A[-1]:
            print('Yes')
            return
    # Third cond: N//3 -> x, N//3 -> y, N//z -> 0 s.t. x^y^z=0
    if N % 3 == 0:
        if A[0] == A[(N//3)-1] and A[N//3] == A[(2*N//3)-1] and A[2*N//3] == A[N-1] \
                and A[0] ^ A[N//3] ^ A[2*N//3] == 0:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    main()