def resolve():
    N, W = list(map(int, input().split()))
    WV = [list(map(int, input().split())) for _ in range(N)]
    wbase = WV[0][0]
    d = {
        wbase: [0],
        wbase+1: [0],
        wbase+2: [0],
        wbase+3: [0],
    }
    for w, v in WV:
        d[w].append(v)
    for v in d.values():
        v.sort(reverse=True)
    
    accs = {}
    for i in range(4):
        accs[wbase+i] = [0]
        for j in range(len(d[wbase+i])):
            accs[wbase+i].append(accs[wbase+i][j]+d[wbase+i][j])
    
    res = 0
    for i in range(len(d[wbase])):
        for j in range(len(d[wbase+1])):
            for k in range(len(d[wbase+2])):
                for l in range(len(d[wbase+3])):
                    if i*wbase+j*(wbase+1)+k*(wbase+2)+l*(wbase+3) <= W:
                        res = max(res, accs[wbase][i]+accs[wbase+1][j]+accs[wbase+2][k]+accs[wbase+3][l])
    print(res)


if __name__ == '__main__':
    resolve()