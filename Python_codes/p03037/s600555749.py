
def solve():
    dp = [0] * N
    L = max(l)
    R = min(r)
    if L <= R:
        i = list(range(L,R+1))
        ans = len(i)
    else:
        ans = 0
    print(ans)

if __name__ == "__main__":
    N,M = list(map(int, input().split()))
#    LR = [list(map(int, input().split())) for _ in range(M)]
    l,r = [0]*M, [0]*M
    for c in range(M):
        tmp = list(map(int, input().split()))
        l[c] = tmp[0]
        r[c] = tmp[1]
    solve()  
