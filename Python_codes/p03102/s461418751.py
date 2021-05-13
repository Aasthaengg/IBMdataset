from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,m,c=map(int,readline().split())
    b=list(map(int,readline().split()))
    a=[list(map(int,readline().split())) for _ in range(n)]

    ans=0
    for i in range(n):
        tmp=c
        for j in range(m):
            tmp+=a[i][j]*b[j]
        if tmp>0:
            ans+=1
    
    print(ans)

if __name__=="__main__":
    main()