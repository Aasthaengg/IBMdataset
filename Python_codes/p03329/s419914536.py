import sys
sys.setrecursionlimit(10**9)


n=int(input())

#dpで解く再帰

memo=[-1]*(n+1)
memo[0]=0

def fuck(x):
    #print(x)
    if memo[x]!=-1:
        return memo[x]
    else:
        tmp=10**9
        #6
        i=1
        while 6**i<=x:
            tmp=min(fuck(x-6**i),tmp)
            i+=1
        #9
        i=1
        while 9**i<=x:
            tmp=min(fuck(x-9**i),tmp)
            i+=1
        #1
        tmp=min(tmp,fuck(x-1))
        memo[x]=tmp+1
        #print(x,tmp+1,memo)
        return tmp+1
fuck(n)
#print(memo)
print(memo[-1])



