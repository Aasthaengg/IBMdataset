from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N=int(readline())
    a=list(map(lambda x:int(x)-1,readline().split()))

    flags=[False]*N
    res=0
    for i in range(N):
        j=a[i]
        if flags[j]==False and a[j]==i:
            flags[i]=True
            flags[j]=True
            res+=1

    print(res)
    
if __name__=="__main__":
    main()