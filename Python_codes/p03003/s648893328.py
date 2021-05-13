

def resolve():
    MOD = int(1e9+7)
    N,M = map(int,input().split())
    S= list(map(int,input().split()))
    T= list(map(int,input().split()))
    dpt = [[0]*(M+1) for i in range(N+1)]

    sm = [[0]*(M+1) for i in range(N+1)]

    for i in range(N):
        for j in range(M):
            dpt[i+1][j+1]= sm[i][j]+1 if S[i]==T[j] else 0

            sm[i+1][j+1] = (sm[i][j+1]+sm[i+1][j]+dpt[i+1][j+1]-sm[i][j]+MOD)%MOD
    ans =0
    for dptr in dpt:
        for i in dptr:
            ans += i
            ans %= MOD

    print(ans+1)            



if __name__ == "__main__":
    resolve()