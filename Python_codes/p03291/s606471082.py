import sys
sys.setrecursionlimit(10**7)
limit = 100000
mod = 10**9+7
lpow = [False] * (limit+1)
lpow[0] = 1
def pow(n,p):
    if p<0:return 0
    if lpow[p]:
        return lpow[p]
    else:
        if p % 2 == 0:
            ret = (pow(n,p//2)**2) % mod
        else:
            ret = ((pow(n,p//2)**2)*n) % mod
        lpow[p] = ret
        return ret

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