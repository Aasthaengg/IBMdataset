def main():
    import sys
    input = sys.stdin.readline
    
    a,b = map(int,input().split())

    #gcd(a,b)の素因数分解
    import math
    gcd = math.gcd(a,b)

    p = []
    for i in range(2,int(math.sqrt(gcd))+1):
        while gcd % i == 0:
            gcd /= i
            p.append(i)
            
    p.append(int(gcd))
    p.append(1)
    print(len(list(set(p))))

if __name__=='__main__':
    main()