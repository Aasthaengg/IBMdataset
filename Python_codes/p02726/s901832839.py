def main():
    N,X,Y=map(int,input().split())

    res=[0 for i in range(N-1)]

    for i in range(1,N):
        for j in range(i+1,N+1):
            if i==j:
                continue
            if (i<=X and j>=Y):
                route=j-i-(Y-X)+1
            else:
                route=min(j-i,abs(X-i)+abs(Y-j)+1)

            res[route-1]+=1

    for r in res:
        print(r)


if __name__=="__main__":
    main()
