

def solve(N, A):
    c = 0
    z = 0
    if A[0] != 0:
        return -1
    for i in range(1, N):
        if A[i] == 0:
            z = 0
            c+=A[i-1]
        elif A[i-1] < A[i] - 1:
            return -1
        elif A[i] <= i - z:
            if A[i] != A[i-1]+1:
                c += A[i-1]
        else:
            return -1
        #print("A[%d]=%d, c=%d" % (i, A[i], c))
    c += A[-1]
    return c

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = [0]*N
    for i in range(N):
        A[i] = int(input())
    print(solve(N, A))

main()
