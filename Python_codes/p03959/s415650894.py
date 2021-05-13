MOD = 10 **9 + 7
INF = 10 ** 10

def main():
    n = int(input())
    T = list(map(int,input().split()))
    A = list(map(int,input().split()))
    mountainT = [-1] * n
    mountainT[0] = T[0]
    for i in range(1,n):
        if T[i - 1] != T[i]:
            mountainT[i] = T[i]
    
    mountainA = [-1] * n
    mountainA[-1] = A[-1]
    for i in range(n - 1,0,-1):
        if A[i - 1] != A[i]:
            mountainA[i - 1] = A[i - 1]
    
    ans = 1
    for i in range(n):
        if mountainA[i] != -1 and mountainT[i] != -1:
            if mountainT[i] != mountainA[i]:
                ans = 0
                break
        elif mountainA[i] != -1:
            if mountainA[i] > T[i]:
                ans = 0
                break
        elif mountainT[i] != -1:
            if mountainT[i] > A[i]:
                ans = 0
                break
        else:
            ans *= min(T[i],A[i])
            ans %= MOD
    print(ans)
if __name__ == '__main__':
    main()