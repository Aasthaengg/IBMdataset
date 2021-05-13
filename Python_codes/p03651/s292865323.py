def main():
    import sys
    input = lambda:sys.stdin.readline().strip()

    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    from math import gcd

    flag = 0
    if K in A: flag = 1
    elif max(A)<K: flag = 0
    else:
        x = max(A)-K
        g = A.pop(0)
        for a in A:
            g = gcd(g,a)

        if K%g==0:
            flag = 1
        
    print(['IMPOSSIBLE','POSSIBLE'][flag])
    


if __name__=='__main__':
    main()