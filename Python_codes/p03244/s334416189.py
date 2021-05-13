from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    v=list(map(int,readline().split()))

    cnt1=[0]*(10**5+1)
    cnt2=[0]*(10**5+1)

    for i in range(n):
        if i%2==0:
            cnt1[v[i]]+=1
        else:
            cnt2[v[i]]+=1

    max1=0
    m=0
    for i in range(1,10**5+1):
        if max1<cnt1[i]:
            max1=cnt1[i]
            m=i
    
    max2=0
    l=0
    for i in range(1,10**5+1):
        if max2<cnt2[i]:
            if i!=m:
                max2=cnt2[i]
                l=i

    max3=0
    o=0
    for i in range(1,10**5+1):
        if max3<cnt2[i]:
            max3=cnt2[i]
            o=i

    max4=0
    p=0
    for i in range(1,10**5+1):
        if max4<cnt1[i]:
            if i!=o:
                max4=cnt1[i]
                p=i

    ans=min(n-max1-max2,n-max3-max4)
    print(ans)

if __name__=="__main__":
    main()