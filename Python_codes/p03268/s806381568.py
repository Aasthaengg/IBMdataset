def main():
    #input data
    import sys
    input = lambda:sys.stdin.readline().strip()
    N,K = map(int,input().split())
    
    #solve
    ans = 0
    for a in range(1,K+1):
        if a == K:
            b = K
            c = K
        else:
            b = K-a
            c = K-a
        if (a+b)%K == 0 and (b+c)%K == 0 and (a+c)%K == 0:
            ans+=((N-a)//K+1)*((N-b)//K+1)*((N-c)//K+1)
    print(ans)
    
if __name__=='__main__':
    main()