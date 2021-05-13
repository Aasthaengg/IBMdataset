n=int(input())
lst=[]

tup = tuple(map(int,input().split()))




m=int(input())

for i in range(m):
    prev,nxt=input().split()
    prev=int(prev)
    nxt=int(nxt)
    lst=list(tup)
    res = 0
    lst[prev-1]=nxt
    for i in range(n):
        res=res+lst[i]
    print(res)


