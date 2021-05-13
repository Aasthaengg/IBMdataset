def main():
    N=int(input())
    A=list(map(int,input().split()))
    ans=1000
    stocks=0
    for i in range(N-1):
        if A[i]>A[i+1]:
            ans+=stocks*A[i]
            stocks=0
        else:
            stocks+=(ans//A[i])
            ans-=(ans//A[i])*A[i]
    print(ans+stocks*A[-1])
if __name__=='__main__':
    main()