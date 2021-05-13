N,M = map(int,input().split())
if(N==1 and M==1):
    print(1)
elif(min(N,M)==1):
    print(max(N,M)-2)
else:
    print(max(N-2,0)*max(M-2,0))