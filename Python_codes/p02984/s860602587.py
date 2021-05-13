def main():
    N = int(input())
    A = list(map(int, input().split()))
    R = [None]*N
    twox = 0
    for i in range(N):
        twox += A[i] * (-1)**i
    R[0] = int(twox)
    for i in range(1, N):
        R[i] = int((A[i-1] - R[i-1]/2)*2)
    print(' '.join(map(str, R)))
main()