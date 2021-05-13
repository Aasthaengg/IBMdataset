def main():
    M,K=map(int, input().split())
    ans=[-1]
    if M==0:
        if K==0:
            ans=[0,0]
    elif M==1:
        if K==0:
            ans=[0,0,1,1]
    else:
        if K<(1<<M):
            L=[i for i in range(1<<M) if i!=K]
            ans=[K]+L+[K]+L[::-1]
    print(*ans)

if __name__ == "__main__":
    main()