h,w,k = map(int, input().split())
s = [input() for _ in range(h)]

def out(l,ll):
    for z in range(ll):
        if l[z] > k:
            return True
    return False

def A(lt, hon):
    noww = [0] * (hon + 1)
    yoko = 0
    for j in range(w):
        kari = [0] * (hon + 1)
        for x in range(hon + 1):
            for y in range(lt[x], lt[x+1]):
                if s[y][j] == "1":
                    kari[x] += 1
        if out(kari, hon+1):
            return h * w
        
        neww = []
        for x in range(hon + 1):
            neww.append(noww[x] + kari[x])
        if out(neww, hon+1):
            yoko += 1
            noww = kari
        else:
            noww = neww
    return yoko + hon

ans = h * w

for i in range(2 ** (h-1)):
    tate = [0]
    honsu = 0
    for j in range(h-1):
        if ((i >> j) & 1):
            tate.append(j + 1)
            honsu += 1
    tate.append(h)
    ans = min(ans, A(tate, honsu))

print(ans)