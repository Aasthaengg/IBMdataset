from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,k=map(int,readline().split())

    if k>(n-1)*(n-2)//2:
        print(-1)
    else:
        m=n-1
        G=[]
        for i in range(2,n+1):
            G.append((1,i))
        cnt=(n-1)*(n-2)//2

        i=2
        j=3
        while k!=cnt:
            G.append((i,j))
            if j<n:
                j+=1
            else:
                i+=1
                j=i+1
            m+=1
            cnt-=1

        print(m)
        for i in range(m):
            print(*G[i])
            
if __name__=="__main__":
    main()