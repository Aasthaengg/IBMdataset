import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [100000] * N
    B = [int(i) for i in input().split()]
    for i in range(N-1):
        if A[i] > B[i]: A[i] = B[i]
        A[i+1] = B[i]
    print(sum(A))
   
    return 0

if __name__ == "__main__":
    solve()