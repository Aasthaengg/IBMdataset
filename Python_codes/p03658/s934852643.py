icase=0
if icase==0:
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    lsum=0
    for i in range(k):
        lsum=lsum+l[i]
    print(lsum)