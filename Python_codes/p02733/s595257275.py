import sys
def main():
    input = sys.stdin.readline
    H,W,K=map(int, input().split())
    oS=[list(map(int, list(input().rstrip()))) for _ in range(H)]

    ans=10**10
    for p in range(1<<(H-1)):
        S=[[oS[i][j] for j in range(W)] for i in range(H)]
        tmp=0
        flag=False
        for i in range(1,H):
            if p&1:
                for j in range(W):
                    S[i][j] += S[i-1][j]
                    if S[i][j]>K: flag=True
            else:
                tmp+=1
            p>>=1
        if flag: continue

        for j in range(W-1):
            for i in range(H):
                if S[i][j]+S[i][j+1]>K:
                    tmp+=1
                    break
            else:
                for i in range(H):
                    S[i][j+1] += S[i][j]

        ans = min(ans, tmp)

    print(ans)

if __name__ == '__main__':
    main()