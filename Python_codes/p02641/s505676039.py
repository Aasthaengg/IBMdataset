X,N=map(int, input().split())
p=list(map(int,input().split()))   
if N==0:
    print(X)
else:
    for k in range(0,51):
        if not X-k in p:
            print(X-k)
            break 
        elif not X+k in p:
            print(X+k)
            break