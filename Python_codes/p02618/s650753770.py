import sys #再帰関数の上限,10**5以上の場合python
import time

t0=time.time()
import random
random.seed(2)
def input(): 
    x=sys.stdin.readline()
    return x[:-1] if x[-1]=="\n" else x
def printe(*x):print(*x,file=sys.stderr)
def printl(li): _=print(*li, sep="\n") if li else None

def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    D = int(input())
    #N, K = map(int, input().split())
    cs = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    S = tuple(tuple(map(int, input().split())) for i in range(D)) #改行行列
    lss=[]
    ls=[0]*26
    anss=[-1]*D
    for i in range(D):
        s=S[i]
        if i==0:
            msc=-1000000
            ans=-1
            for j in range(26):
                sc=s[j]+cs[j]

                if msc<sc:
                    ans=j
                    msc=sc
            ls[ans]=1
            #lss.append(ls)
            anss[i]=ans+1
            continue
        msc=0
        ans=-1
        dec=[-cs[j]*(i+1-ls[j]) for j in range(26)]
        msc=-10000000
        ans=-1
        for j in range(26):
            sc=s[j]-dec[j]
            if msc<sc:
                ans=j
                msc=sc
        ls[ans]=i+1
        #lss.append(ls)
        anss[i]=ans+1
    
    def eval(anss):
        ls=[0]*26
        score=0
        for i in range(D):
            j=anss[i]-1
            ls[j]=i+1
            score+=S[i][j]
            dec=sum([cs[k]*(i+1-ls[k]) for k in range(26)])
            score-=dec
        return score
    
    def eval2(anss,score,target,val,pval):
        score=score-S[target][pval-1]+S[target][val-1]
        f1=0
        f2=0
        cp=cv=-1
        if target>0:
            for i in range(target-1,-1,-1):
                a=anss[i]
                if a==pval and not f1:
                    cp=i
                    f1=1
                elif a==val and not f2:
                    cv=i
                    f2=1
                if f1 and f2:
                    break
        f1=f2=0
        
        csv=cs[val-1]
        csp=cs[pval-1]
        tcv=(target-cv)*csv
        tcp=(target-cp)*csp
        score+=tcv-tcp
        for i in range(target+1,D):
            a=anss[i]
            if anss[i]==pval and not f2:
                f2=1
            elif anss[i]==val and not f1:
                f1=1
            if not f1:
                score+=tcv
            if not f2:
                score-=tcp
            if f1 and f2:
                break
        return score

    
    csc=eval(anss)
    #nans=copy(anss)

    
    yaki=1000.0
    count=0
    abest=anss.copy()
    tsc=csc
    lc=0
    mc=10000
    while 1:
        count+=1
        target=random.randrange(0,D)
        pval=anss[target]
        target2=target
        pval2=pval
        while pval2==pval:
            target2=random.randrange(0,D)
            pval2=anss[target2]

        val=pval
        val2=pval2
        while val==pval or val==pval2:
            val=random.randrange(0,26)+1
        while val2==pval or val2==pval2 or val2==val:
            val2=random.randrange(0,26)+1
        
        #val=pval
        #nans[target]=val
        #printe(target,val,pval,target2,val2,pval2)
        nsc=eval2(anss,tsc,target,val,pval)
        nsc=eval2(anss,nsc,target2,val2,pval2)
        
        if nsc>csc:
            csc=nsc
            tsc=nsc
            anss[target]=val
            anss[target2]=val2
            abest=anss.copy()
            lc=count
        else:           
            r=random.random()
            if r<2**(-(csc-nsc)/(yaki+1e-9)):
                anss[target]=val
                anss[target2]=val2
                tsc=nsc
            if count-lc>mc:
                anss=abest.copy()
                tsc=csc
                lc=count

        if time.process_time()>1.95:
            break
    printl(abest)
    return
    #printe(csc,count,lc,abest[0])
    #printe(eval(anss))
    

if __name__ == "__main__":
    main()