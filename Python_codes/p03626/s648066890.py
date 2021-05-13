def main():
    n=int(input())
    domino=[list(input()) for i in range(2)]
    mod=10**9+7

    if domino[0][0]==domino[1][0]:
        dp=[3]
        i=1
        before=True
    else:
        dp=[6]
        i=2
        before=False

    while i<n:
        if domino[0][i]==domino[1][i]:
            if before:
                nex=dp[-1]*2%mod
                dp.append(nex)
            else:
                nex=dp[-1]%mod
                dp.append(nex)
            before=True
            i+=1
        else:
            if before:
                nex=dp[-1]*2%mod
                dp.append(nex)
            else:
                nex=dp[-1]*3%mod
                dp.append(nex)
            before=False
            i+=2
    print(dp[-1])
if __name__=='__main__':
    main()