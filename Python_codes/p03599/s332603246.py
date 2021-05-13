a, b, c, d, e, f = map(int, input().split())

max_nodo = 0
ans = [100*a, 0]
for i in range(30//a+1):
    for j in range(30//b+1):
        mizu = 100*i*a + 100*j*b
        if mizu > f: break
        if mizu == 0: continue
        maxi = (i*a + j*b) * e
        for k in range(maxi//c+1):
            for l in range(maxi//d+1):
                sato = c*k + d*l
                if mizu+sato > f: break
                if sato > maxi: break
                nodo = sato / (mizu+sato)
                if nodo > max_nodo:
                    max_nodo = nodo
                    ans = [mizu+sato, sato]

print(ans[0], ans[1])