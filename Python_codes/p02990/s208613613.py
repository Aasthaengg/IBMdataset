n, k = map(int, input().split())

def cmb(s, t, r):
    x = 1
    y = 1
    for i in range(t):
        x = (x*(s-i))%r
        y = (y*(i+1))%r
 
    y_inverse = pow(y, r-2, r)
    return (x*y_inverse)%r

mod = 10 ** 9 + 7

for i in range(1,k+1):
    div = cmb(k-1, i-1,mod)
    red = n + 1 - k - i 
    if red < 0:
        print(0)
        continue
    pat = cmb(i+red,red,mod)
    ans = (div * pat) % mod
    print(ans)