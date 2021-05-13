def ng():
    print(-1)
    exit()

def main():
    N,*P=map(int, open(0).read().split())
    ans=0
    pre=0
    if P[0]!=0: ng()
    for p in P[1:]:
        if pre+1<p: ng()
        ans+=1 if pre+1==p else p
        pre=p
    print(ans)

if __name__ == "__main__":
    main()