
def solve():
    dp = [0] * N
    for i in range(Q):
        dp[A[i]-1] += 1
    for j in range(N):
        if K - (Q - dp[j]) > 0:
            print("Yes")
        else:
            print("No")
#    print(dp)

if __name__ == "__main__":
    N,K,Q = list(map(int, input().split()))
    A = [int(input()) for _ in range(Q)]
    solve()  
