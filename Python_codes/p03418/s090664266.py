def solve(N,K):
    if K == 0:
        return N**2
    else:
        ans = 0
        for b in range(K+1,N+1):
            #b <= a <= Nで a mod b >= Kを満たすaの個数
            q,r = N//b,N%b
            ans += (q*(b-K) + max(0,r-K+1))
        return ans

def main():
    N,K = map(int,input().split())

    print(solve(N,K))

if __name__ == "__main__":
    main()
