def main():
    X,Y,A,B,C=map(int,input().split())
    P=list(map(int,input().split()))
    Q = list(map(int, input().split()))
    R = list(map(int, input().split()))

    P.sort(reverse=True)
    Q.sort(reverse=True)
    R.sort(reverse=True)
    Pmax=P[:X]
    Qmax=Q[:Y]

    Pmax.extend(Qmax)
    Pmax.extend(R)
    Pmax.sort(reverse=True)
    res=0
    for i in range(X+Y):
        res+=Pmax[i]

    print(res)

if __name__=="__main__":
    main()


