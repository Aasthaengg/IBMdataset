def minandmax(bottom,up,mod): #bottom< n < upなるmodで割り切れるnの値の最大値と最小値を返す
    if bottom%mod == 0:
        mnm = bottom
    else:
        mnm = bottom + (mod-bottom%mod)
        if mnm > up:
            mnm = None
    if up%mod == 0:
        mxm = up
    else:
        mxm = up - up%mod
        if mxm < bottom:
            mxm = None
    ans = [mnm,mxm]
    return ans

k = int(input())
a = list(map(int,input().split()))
i = k-1
bottom = 2
up = 2

check = True
if a[-1] != 2:
    check = False
while i >= 1 and check:
    nbottom = minandmax(bottom,up+a[i]-1,a[i-1])[0]
    nup = minandmax(bottom,up+a[i]-1,a[i-1])[1]
    if nbottom == None and nup == None:
        check = False
    elif nbottom == None:
        nbottom = nup
    elif nup == None:
        nup = nbottom
    i += -1
    bottom = nbottom
    up = nup

if check:
    bottom = minandmax(bottom,bottom+a[0]-1,1)[0]
    up = minandmax(up,up+a[0]-1,1)[1]
    print(bottom,up)
else:
    print("-1")