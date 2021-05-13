MOD = 10 ** 9 +7
h, w, k = map(int,input().split())

if w == 1:
    print(1)
else:
    acr = []
    for p in range(2**(w-1)):
        det = 0
        pp = p
        exist = [0] * (w-1)
        for i in range(w-1):
            exist[i] = pp % 2
            pp = pp // 2
        for ii in range(w-2):
            if exist[ii] == 1 and exist[ii+1] == 1:
                det = 1
        if det == 0:
            acr.append(exist[:])
    #print(acr)

    cur = [0] * w
    cur[0] = 1
    

    for t in range(h):
        n = [0] * w
        for x in range(len(acr)):
            n[0] = (n[0] + cur[1] * acr[x][0] + cur[0] * (1-acr[x][0]))%MOD
            for j in range(1,w-1):
                n[j] = (n[j] + cur[j-1] * acr[x][j-1] + cur[j+1] * acr[x][j] + cur[j] * (1-acr[x][j-1])*(1-acr[x][j]))%MOD
            n[w-1] = (n[w-1] + cur[w-2] * acr[x][w-2] + cur[w-1] * (1-acr[x][w-2])) % MOD
        
        cur = n[:]
        
    print(cur[k-1])