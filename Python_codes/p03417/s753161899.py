N,M=map(int,input().split())
if N==1 or M==1:
    if N*M==1:
        print(1)
    else:
        print(max(N*M-2,0))
else:
    print(max((N*M)-N*2-M*2+4,0))