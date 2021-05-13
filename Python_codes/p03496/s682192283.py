N = int(input())
A = list(map(int,input().split()))
mi = min(A)
ma = max(A)
g = 1
if mi > 0:
    g = 1
elif ma < 0:
    g = -1
elif abs(mi) < abs(ma):
    g = 1
else:
    g = -1

print(2*N-1)
if g == 1:
    mai = A.index(ma)
    print(mai+1,mai+1)
    A[mai] += A[mai]
    #print(A)
    for i in range(N):
        if i != mai:
            print(mai+1,i+1)
            A[i] += A[mai]
            #print(A)
    for i in range(N-1):
        print(i+1,i+2)
        A[i+1] += A[i]
        #print(A)
else:
    mii = A.index(mi)
    print(mii+1,mii+1)
    A[mii] += A[mii]
    #print(A)
    for i in range(N):
        if i != mii:
            print(mii+1,i+1)
            A[i] += A[mii]
            #print(A)
    for i in range(N-1,0,-1):
        print(i+1,i)
        A[i-1] += A[i]
        #print(A)
