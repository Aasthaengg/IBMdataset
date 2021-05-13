import sys
sys.setrecursionlimit(90000)
n,K=map(int,input().split())
visitedlist=[-1 for  i in range(n)]
kilist=[[] for i in range(n)]
anslist=[0 for i in range(n)]
searchedlist=[-1 for i in range(n)]
for i in range(n-1):
        a,b=map(int,input().split())
        kilist[a-1].append(b)
        kilist[b-1].append(a)
def search(P):
        searchedlist[P-1]=1
        visitedlist[P-1]=1
        flag=0
        for j in kilist[P-1]:
            if visitedlist[j-1]<0:
                visitedlist[j-1]=1
                flag+=1
                anslist[j-1]=anslist[P-1]+1
        else:
            pass

        if flag>0:    
            for k in kilist[P-1]:
                if searchedlist[k-1]==-1:
                    search(k)
def find_power(n):
    # 0!からn!までのびっくりを出してくれる関数
    powlist=[0]*(n+1)
    powlist[0]=1
    powlist[1]=1
    for i in range(2,n+1):
        powlist[i]=powlist[i-1]*i%(10**9+7)
    return powlist
def find_inv_power(n):
    #0!からn!までの逆元を10**9+7で割ったあまりリストを作る関数
    powlist=find_power(n)
    check=powlist[-1]
    first=1
    uselist=[0]*(n+1)
    secondlist=[0]*30
    secondlist[0]=check
    secondlist[1]=check**2
    for i in range(28):
        secondlist[i+2]=(secondlist[i+1]**2)%(10**9+7)
    a=format(10**9+5,"b")
    for j in range(30):
        if a[29-j]=="1":
            first=(first*secondlist[j])%(10**9+7)
    uselist[n]=first
    for i in range(n,0,-1):
        uselist[i-1]=(uselist[i]*i)%(10**9+7) 
    return uselist
search(1)
power=find_power(100000)
invpower=find_inv_power(100000)
distancelist=[(i+1,anslist[i]) for i in range(n)]
distancelist=sorted(distancelist,key=lambda x:x[1])
answer=1
for some in distancelist:
    if some[1]==0:
        answer*=K
        howmuch=len(kilist[some[0]-1])   
        if K-1<howmuch:
            answer=0
            break
        else:
            answer=answer*power[K-1]*invpower[K-1-howmuch]
            answer=answer%(10**9+7)        
    else:
        howmuch=len(kilist[some[0]-1])-1
        if howmuch==0:
            pass
        else:
            if K-2<howmuch:
                answer=0
                break
            else:
                answer=answer*power[K-2]*invpower[K-2-howmuch]
                answer=answer%(10**9+7)
print(answer)
