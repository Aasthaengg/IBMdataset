INF=float("inf")
def c2i(c): return ord(c)-ord("a")

def main():
    S=list(map(c2i, input()))
    N=len(S)
    T=list(map(c2i, input()))
    S*=2
    Next=[[INF]*26 for _ in range(N*2)]
    for i in range(N*2-2,-1,-1):
        for j in range(26):
            Next[i][j] = 1 if S[i%N]==j else Next[i+1][j]+1
    ans=0
    i=0
    for t in T:
        x=Next[i][t]
        if x==INF:
            print(-1)
            exit()
        i+=x
        i%=N
        ans+=x
    print(ans)


if __name__ == "__main__":
    main()