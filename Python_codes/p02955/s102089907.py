def main():
    N,K,*A=map(int, open(0).read().split())
    S=sum(A)
    X=[S]
    for i in range(2,int(S**.5)+1):
        if S%i==0:
            X.append(i)
            if i*i!=S:
                X.append(S//i)
    ans=1
    for x in X:
        B=[a%x for a in A]
        y=sum(B)//x
        z=sum(sorted(B, reverse=True)[y:])
        if z<=K:
            ans=max(ans,x)
    print(ans)

if __name__ == "__main__":
    main()