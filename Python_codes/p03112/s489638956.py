import bisect
a,b,q=map(int,input().split())
shrines=[-10**20]+[int(input()) for i in range(a)]+[10**20]
temples=[-10**20]+[int(input()) for i in range(b)]+[10**20]
for i in range(q):
    x=int(input())
    s=bisect.bisect_left(shrines,x)
    t=bisect.bisect_left(temples,x)
    Dsleft=x-shrines[s-1]
    Dtleft=x-temples[t-1]
    Dsright=shrines[s]-x
    Dtright=temples[t]-x
    print(min(max(Dsleft,Dtleft),max(Dsright,Dtright),Dsleft+Dtright+min(Dsleft,Dtright),Dsright+Dtleft+min(Dsright,Dtleft)))