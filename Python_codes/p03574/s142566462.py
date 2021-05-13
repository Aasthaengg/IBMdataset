def main():
    H,W = map(int,input().split())
    S = list()
    INF = 10**18
    S.append([-INF]*(W+2))
    for i in range(H):
        line = list(input())
        for j,c in enumerate(line):
            if c == '.':
                line[j] = 0
            else:
                line[j] = -INF

        S.append([-INF]+line+[-INF])
    S.append([-INF]*(W+2))
    for i in range(1,H+1):
        for j in range(1,W+1):
            if S[i][j] < 0:
                S[i-1][j-1] += 1
                S[i-1][j] += 1
                S[i-1][j+1] += 1
                S[i][j-1] += 1
                S[i][j+1] += 1
                S[i+1][j-1] += 1
                S[i+1][j] += 1
                S[i+1][j+1] += 1
    
    out = ''
    for i in range(1,H+1):
        for j in range(1,W+1):       
            out += '#' if S[i][j] < 0 else str(S[i][j])
        out += '\n'
    print(out)
                
main()