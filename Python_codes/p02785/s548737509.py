n,k=map(int,input().split())
h=list(map(int,input().strip().split()))[:n]
h.sort()
if(k>=n):
    print(0)

elif(k==0):
    b=sum(h)
    print(b)
elif(k<n):
    b=sum(h[:-k])
    print(b)