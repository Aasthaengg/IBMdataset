mod = 10**9+7
def pow(n,p):
    res=1
    while p >0:
        if p%2==0:
            n = n**2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod

def main():
    s=input()
    res = 0
    ca = 0
    cc = s.count("C")
    cw = 0
    aw = s.count("?")
    for c in s:
        if c == "A":
            ca += 1
        elif c == "C":
            cc -= 1
        elif c == "B":
            res += ca*cc*pow(3,aw)+ca*(aw-cw)*pow(3,aw-1)+cw*cc*pow(3,aw-1)+cw*(aw-cw)*pow(3,aw-2)
            res %= mod
        elif c == "?":
            res += ca*cc*pow(3,aw-1)+ca*(aw-cw-1)*pow(3,aw-2)+cw*cc*pow(3,aw-2)+cw*(aw-cw-1)*pow(3,aw-3)
            res %= mod
            cw += 1

    print(res)

main()