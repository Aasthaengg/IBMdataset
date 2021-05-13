
if __name__ == '__main__':
    N = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans = 1
    if T[0] > A[0] or T[N-1] < A[N-1]:
        ans = 0
    for i in range(N-1):
        if T[i] > T[i+1]:
            ans = 0
        if T[i] < T[i+1] and T[i+1] > A[i+1]:
            ans = 0
    for i in range(N-1, 0, -1):
        if A[i] > A[i-1]:
            ans = 0
        if A[i] < A[i-1] and A[i-1] > T[i-1]:
            ans = 0
    for i in range(1, N-1):
        if T[i] != T[i-1] or A[i] != A[i+1]:
            continue
        else:
            ans *= min(A[i], T[i])
            ans %= int(1e9+7)
    print(ans)