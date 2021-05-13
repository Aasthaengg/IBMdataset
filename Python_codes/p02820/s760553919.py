def main():
    N,K=map(int,input().split())
    R,S,P=map(int,input().split())
    T=input()

    res=0
    T_=[]
    for i in range(N):
        if T[i]=="r":
            res+=P
            T_.append("p")
        elif T[i]=="s":
            res+=R
            T_.append("r")
        else:
            res+=S
            T_.append("s")
    for i in range(N):
        if i>=K:
            if T_[i-K]==T_[i]:
                if T_[i]=="r":
                    res-=R
                elif T_[i]=="s":
                    res-=S
                else:
                    res-=P
                T_[i]="#"

    print(res)

if __name__=="__main__":
    main()
