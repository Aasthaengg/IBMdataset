
        
def f3(N,S,M):
    sm=S//M
    l=[]
    for i in range(M):
        l.append([])
    li=[i for i in range(1,N+1)]
    for x in range(M):
        tmp=0
        for i in reversed(range(N)):
            if li[i]==-1:
                continue
            tmp+=li[i]
            if tmp>sm:
                tmp-=li[i]
                if li[sm-tmp-1]==-1:
                    #print(N,sm,"!!!")
                    return
                l[x].append(sm-tmp)
                li[sm-tmp-1]=-1
                break
            l[x].append(li[i])
            li[i]=-1
            if tmp==sm:
                break
    y=0
    for x in range(M):
        y+=len(l[x])*(N-len(l[x]))
    y//=2
    print(y)
    for x in range(M):
        for xi in l[x]:
            for y in range(x+1,M):
                for yi in l[y]:
                    print(xi,yi)
    
    
def min_factor(S):
    for i in range(2,101):
        if S%i==0:
            return i

#24,39

N=int(input())
S=N*(N+1)//2
M=min_factor(S)
f3(N,S,M)