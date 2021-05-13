from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N,M=map(int,readline().split())
    ab=[0]*M
    for i in range(M):
        ab[i]=list(map(int,readline().split()))

    ab.sort(key=lambda x:x[1])
    res=0
    for i in range(M):
        a=ab[i][0]
        b=ab[i][1]
        if i==0:
            bridge=b-1
            res+=1
        else:
            if a<=bridge:
                pass
            else:
                bridge=b-1
                res+=1
    
    print(res)

if __name__=="__main__":
    main()