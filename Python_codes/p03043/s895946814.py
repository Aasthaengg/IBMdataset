
def solve():
    scr_ini = list(range(1,N+1))
#    print(scr_ini)
    cnt = [0] * N
    ans = [0] * N
    for i in range(N):
        j = 0
        while scr_ini[i]*2**j < K:
            cnt[i] = j
            j += 1
        if scr_ini[i]*2**j >= K:
            cnt[i] = j
            ans[i] = (1/N) * 0.5**j
#    print(cnt) 
#    print(ans)
    print(sum(ans))

if __name__ == "__main__":
    N,K = list(map(int, input().split()))
    solve()  
