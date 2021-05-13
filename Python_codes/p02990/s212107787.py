n, k = map(int, input().split())
mod = 10 ** 9 + 7
 
 
def cmb(n, r):

    # print("nsr",n,r)
    if (r < 0): return 0 
    if (n < 0): return 1
    if (n < r): return 0


    r = min(r, n - r)
    x = 1
    y = 1
    for i in range(r):
        x = x * (n - i) % mod
        y = y * (i + 1) % mod
    y = pow(y, mod-2, mod)
    return x * y % mod
 

for i in range(1,k+1):
    x,y = k,i
    blue = cmb(x-1,x-y)
    # print("bbbbbb",blue)

    red=0
    
    x,y = n-k,i-1
    red+=cmb(x-1,x-y)
    # print(red)

    x,y = n-k,i
    red+=cmb(x-1,x-y)
    red+=cmb(x-1,x-y)
    # print(red)

    x,y = n-k,i+1
    red+=cmb(x-1,x-y)
    # print(red)

    # print("ans",blue*red%mod)
    print(blue*red%mod)
