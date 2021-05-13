icase=0
if icase==0:
    n=int(input())
    v=list(map(int,input().split()))
    c=list(map(int,input().split()))
    tmax=0
    for i in range(n):
        total = 0
        for j in range(n):
            total = total+max(0,v[j]-c[j])   
        tmax=max(tmax,total)
    print(tmax)