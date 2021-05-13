N=int(input())
A=list(map(int,input().split()))
A=A[::-1]
dpmax=[0 for i in range(0,N)]
dpmin=[0 for i in range(0,N)]

for i in range(0,N):
    if i==0:
        if A[0]!=2:
            print(-1)
            break
        else:
            dpmax[0]=3
            dpmin[0]=2
    else:
        testmax=dpmax[i-1]-dpmax[i-1]%A[i]
        if dpmin[i-1]%A[i]!=0:
            testmin=dpmin[i-1]-dpmin[i-1]%A[i]+A[i]
        else:
            testmin=dpmin[i-1]
        if testmax>=dpmin[i-1]:
            dpmax[i]=testmax+A[i]-1
        else:
            print(-1)
            break
        if dpmax[i-1]>=testmin:
            dpmin[i]=testmin
        else:
            print(-1)
            break
else:
    print(dpmin[-1],dpmax[-1])
