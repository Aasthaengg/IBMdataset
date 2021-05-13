import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    T = [int(t) for t in input().split()]
    A = [int(a) for a in input().split()]
    mod = 7 + 10 ** 9
    Ans = 1
    H = [-1] * N
    H[0] = T[0]
    for i in range(1, N):
        if T[i] > T[i-1]: H[i] = T[i]
    if H[N-1] > -1 and H[N-1] != A[N-1]: Ans = 0
    else: H[N-1] = A[N-1]
    for i in reversed(range(N-1)):
        if A[i] > A[i+1]:
            if H[i] > -1 and H[i] != A[i]: Ans = 0
            elif T[i] < A[i]: Ans = 0
            else: H[i] = A[i]
        else:
            if H[i] == -1: 
                Ans *= min(T[i], A[i])
                Ans %= mod
    print(Ans)
            
    return 0

if __name__ == "__main__":
    solve()