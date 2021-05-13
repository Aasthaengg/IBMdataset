def main():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]
    piyo = []
    result = [[0]*W for _ in range(H)]
    hoge = 0
    pesi = 0
    for i in range(H):
        temp = S[i].count("#")
        if temp > 0:
            for j in range(W):
                if S[i][j] == "#":
                    hoge += 1
                for k in range(pesi+1):
                    result[i-k][j] = hoge
            temp = S[i].find("#")
            guhu = result[i][temp]
            for j in range(temp):
                for k in range(pesi+1):
                    result[i-k][j] = guhu
            pesi = 0
        else:
            pesi += 1
    for j in range(W):
        for k in range(1, pesi+1):
            result[-k][j] = result[-pesi-1][j]
    for r in result:
        r = map(str, r)
        print(" ".join(r))
main()