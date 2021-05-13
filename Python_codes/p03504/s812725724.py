def main():
    import sys
    input = sys.stdin.readline
    
    N,C = map(int,input().split())
    STC = []
    B = [[0]*(10**5+1) for _ in range(C)]
    for i in range(N):
        s,t,c = map(int,input().split())
        for j in range(s,t+1):
            B[c-1][j] = 1
    
    x = 0
    flag = 1
    nowc = -1
    while flag == 1:
        flag = 0
        x += 1
        nowc = -1
        for i in range(1,10**5+1):
            if nowc != -1:
                if B[nowc][i] == 1:
                    B[nowc][i] = 0
                else:
                    nowc = -1
                    for j in range(C):
                        if B[j][i] == 1:
                            nowc = j
                            B[j][i] = 0
                            break
            else:
                for j in range(C):
                    if B[j][i] == 1:
                        flag = 1
                        nowc = j
                        B[j][i] = 0
                        break
    print(x-1)

main()    