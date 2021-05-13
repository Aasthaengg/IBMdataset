import math
def main():
    a,b,c,d = map(int,input().split())
    bc = b // c
    bd = b // d
    bx = b // (c * d // math.gcd(c,d))
    B = b - bc - bd + bx
    
    a -= 1
    ac = a // c
    ad = a // d
    ax = a // (c * d // math.gcd(c,d))
    A = a - ac - ad + ax
    
    print(B-A)
    
if __name__ == "__main__":
    main()