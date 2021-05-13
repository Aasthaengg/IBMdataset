#n=int(input())
n,m,q=map(int,input().split())
al=[0]*q
bl=[0]*q
cl=[0]*q
dl=[0]*q
for i in range(q):
    al[i],bl[i],cl[i],dl[i]=map(int,input().split())

def score(A):
    res=0
    for ai,bi,ci,di in zip(al,bl,cl,dl):
        if A[bi-1]-A[ai-1]==ci:
            res+=di
    return res
scorelist=[]
def dfs(A):
    global scorelist
    lastone=A[-1] if len(A)>0 else 1
    if len(A)==n:
        scorelist.append(score(A))
        return 
    for v in range(lastone,m+1):
        A.append(v)
        dfs(A)
        A.pop()

dfs([])
print(max(scorelist))
