import itertools
INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    ans=0
    n=INT()
    A=[]
    for i in range(n):
        a=INT()
        A.append([])
        for k in range(a):
            x,y=INTM()
            x-=1
            A[i].append([x,y])

    #print(A)

    for i in itertools.product([0,1], repeat=n):
        #print(str(sum(i))+'aaaa')
        flg=True
        for k in range(n):
            if i[k]==1:
                for j in A[k]:
                    if i[j[0]]!=j[1]:
                        flg=False
                        break
        
        if flg:
            ans=max(ans,sum(i))

    print(ans)


if __name__=='__main__':
    do()