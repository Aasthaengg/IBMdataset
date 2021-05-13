N,K = map(int,input().split())
MOD = 10**9+7
a = list(map(int,input().split()))
b = []
c = []
d = []
num_z = 0
for val in a:
    if val>0:
        b.append(val)
        d.append(val)
    elif val<0:
        c.append(-val)
        d.append(-val)
    else:
        num_z += 1
        d.append(0)
num_b = len(b)
num_c = len(c)
res = 1
if (N==num_c and K%2==1):
    d = sorted(d)
    for val in d[:K]:
        res = res*val%MOD
    res = -res%MOD
elif (N==K and num_c>0):
    c = sorted(c)
    for val in a:
        res = res*val%MOD
elif num_b==0:
    if K%2==0:
        if num_c >= K:
            c = sorted(c,reverse=True)
            for val in c[:K]:
                res = res*val%MOD
        else:
            res = 0
    else:
        res = 0
else:
    b = sorted(b,reverse=True)
    c = sorted(c,reverse=True)
    bidx = 0
    cidx = 0
    tmp = 0
    if num_b+num_c < K:
        res = 0
    else:
        if num_b >= K:
            bidx = K
        elif num_c>=2:
            bidx = num_b
            cidx = K-bidx
            if (K-num_b)%2==1:
                if cidx == num_c:
                    print(0)
                    exit()
                bidx -= 1
                cidx += 1
        else:
            print(0)
            exit()
        #print(bidx,cidx)
        for val in b[:bidx]:
            res = res*val%MOD
        for val in c[:cidx]:
            res = res*val%MOD
        for k in range(100000):
            if bidx<=1 or cidx+1 >= num_c:
                break
            if b[bidx-1]*b[bidx-2] > c[cidx]*c[cidx+1]:
                break
            else:
                res *= c[cidx]
                res *= c[cidx+1]
                res = res%MOD
                res = res*pow(b[bidx-1],MOD-2,MOD)
                res = res*pow(b[bidx-2],MOD-2,MOD)
                res = res%MOD
                bidx -= 2
                cidx += 2
print(res%MOD)

