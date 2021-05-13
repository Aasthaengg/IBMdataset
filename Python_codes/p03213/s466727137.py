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
    n=int(readline())

    d=dict()
    for i in range(1,n+1):
        li=fac(i)
        for p in li:
            if p[0] not in d:
                d[p[0]]=p[1]
            else:
                d[p[0]]+=p[1]

    cnt_75=0
    cnt_25=0
    cnt_15=0
    cnt_5=0
    cnt_3=0
    for v in d.values():
        if v>=74:
            cnt_75+=1; cnt_25+=1; cnt_15+=1; cnt_5+=1; cnt_3+=1
        elif v>=24:
            cnt_25+=1; cnt_15+=1; cnt_5+=1; cnt_3+=1
        elif v>=14:
            cnt_15+=1; cnt_5+=1; cnt_3+=1
        elif v>=4:
            cnt_5+=1; cnt_3+=1
        elif v>=2:
            cnt_3+=1

    ans=0
    ans+=cnt_75
    ans+=cnt_25*(cnt_3-1)
    ans+=cnt_15*(cnt_5-1)
    ans+=cnt_5*(cnt_5-1)//2*(cnt_3-2)
    print(ans)

if __name__=="__main__":
    main()