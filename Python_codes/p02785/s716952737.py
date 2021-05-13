n,k=map(int,input().split())
h=map(int,input().split())
s=0
if n <= k:
    print("0")
else:
    if k==0:
        s=sum(h)
        print(s)
    else: 
        x=sorted(h)
        for i in range (0, k):
            x.pop()
        s=sum(x)
        print(s)        
