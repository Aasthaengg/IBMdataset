


def resolve():
    N=int(input())
    A=list(map(int,input().split()))

    l=0
    r=0
    summury=0
    sv=0
    while r<=N-1:
        if sv+A[r] == sv ^ A[r]:
            #print(l,r,"#")
            sv+=A[r]
            r+=1

        else:

            cc=r-l
            summury+=cc
            #print(l,r,summury)
            if l==r:
                r+=1
            else:
                sv-=A[l]
                l+=1


    cc=r-l+1
    summury+=(cc-1)*cc//2
    print(summury)



if __name__ == "__main__":
    resolve()