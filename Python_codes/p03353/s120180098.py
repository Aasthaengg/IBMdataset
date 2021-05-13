def main2():
    S=list(input())
    K=int(input())
    N=len(S)

    P=sorted(S)
    l=[]
    a=[]
    k=0
    while len(l)<=5 and k<N:
        if P[k] not in a:
            a.append(P[k])
            for n in range(N):
                if S[n]==P[k]:
                    for i in range(1,6):
                        if n+i<=N:
                            tmp="".join(S[n:n+i])
                            if tmp not in l:
                                l.append(tmp)
        k+=1
    l.sort()
    print(l[K-1])

if __name__=="__main__":
    main2()