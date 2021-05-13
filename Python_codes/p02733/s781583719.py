h,w,kk = map(int,input().split())
s = [list(map(int, input())) for i in range(h)]

ans = h+w-2
for i in range(1 << (h-1)):
    tate = 0
    index = [0] * h
    # しきりはh-1個なので2個目から考える
    for j in range(h-1):
        if i & (1 << j):
            tate += 1
        index[j+1] = tate # チョコ軍の番号
    chocos = [0]*(tate + 1) # チョコ軍
    yoko = 0
    ok = True
    for j in range(w):
        for k in range(h):
            chocos[index[k]] += s[k][j]
            # kkを超えるたびにその直前に仕切りをいれて新しいチョコ軍について考える
        if max(chocos) > kk:
            yoko += 1
            chocos = [0]*(tate+1)
            for l in range(h):
                chocos[index[l]] += s[l][j]
            if max(chocos) > kk:# その列だけで超える
                ok = False
        if not ok:
            break
    if ok:
        ans = min(ans, tate + yoko)

print(ans)