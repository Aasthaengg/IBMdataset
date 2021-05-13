def main():
    import sys
    input = sys.stdin.readline

    N,Y = map(int,input().split())
    
    Y //= 1000
    for i in range(N+1):
        for j in range(N+1-i):
            k = (N-i-j)
            m = i*10 + j*5 + k*1
            if m == Y:
                print("{} {} {}".format(i,j,k))
                return
    print("-1 -1 -1")

if __name__ == '__main__':
    main()
