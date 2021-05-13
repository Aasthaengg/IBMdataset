N,M=map(int,input().split())
if(N==1 or M==1):
    print(abs(max(N,M)-2))
else:
    print(N*M+4-(2*M)-(2*N))