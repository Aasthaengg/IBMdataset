def fac(n):  #nは2以上
    a=[]
    t=n
    if t%2==0:
        count=0
        while t%2==0:
            count+=1
            t//=2
        a.append([2,count])

    for i in range(3,n+1,2):
        if i*i>n:
            break
        if t%i==0:
            count=0
            while t%i==0:
                count+=1
                t//=i
            a.append([i,count])

    if t!=1:
        a.append([t,1])
    
    return a


from sys import stdin
def main():
    #入力
    readline=stdin.readline
    mod=10**9+7
    n=int(readline())

    d=dict()
    for i in range(1,n+1):
        tmp=fac(i)
        for j in range(len(tmp)):
            if tmp[j][0] not in d:
                d[tmp[j][0]]=tmp[j][1]
            else:
                d[tmp[j][0]]+=tmp[j][1]

    ans=1
    for v in d.values():
        ans*=(v+1)
        ans%=mod

    print(ans)

if __name__=="__main__":
    main()