import sys
input = sys.stdin.readline

def main():
    N = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))
    if T[0] <= A[0] and A[N-1] <= T[N-1]:
        ans = 1
    else:
        return 0
    MOD = int(1e9) + 7
    for i in range(1, N-1):
        t = (T[i] == T[i-1])
        a = (A[i] == A[i+1])
        if not(t) and not(a):
           if T[i] != A[i]:
               return 0
        elif not(t) and a:
            if A[i] < T[i]:
                return 0
        elif t and not(a):
            if T[i] < A[i]:
                return 0
        else:
            ans *= min(T[i], A[i])
            ans %= MOD
    
    return ans

if __name__ == "__main__":
    print(main())