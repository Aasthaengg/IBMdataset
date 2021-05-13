from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))  #葉の数

    s=[0]*(n+1)
    for i in range(n,-1,-1):
        if i==n:
            s[i]=a[i]
        else:
            s[i]+=a[i]+s[i+1]

    b=[0]*(n+1)  #葉でない頂点数
    res=0
    flag=True
    for i in range(n+1):
        if i==0:
            if a[i]>=2:
                flag=False
                break
            if a[i]==1: b[i]=0
            else: b[i]=1
            res+=1
        else:
            v_max=min(s[i],2*b[i-1])
            if v_max<a[i]:
                flag=False
                break
            else:
                b[i]=v_max-a[i]
                res+=v_max
    
    if flag:
        print(res)
    else:
        print(-1)

if __name__=="__main__":
    main()