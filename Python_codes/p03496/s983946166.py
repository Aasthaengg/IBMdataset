N = int(input())
A = list(map(int,input().split()))
Amax = max(A)
Amin = min(A)
outlis=[];

if Amin > 0:
    print(N-1)
    for i in range(N-1):
        print(i+1,i+2) 
elif Amax < 0:
    print(N-1)
    for i in range(N-1):
        print(N-i,N-i-1)
else:
    print(2*N-2)
    if abs(Amax) > abs(Amin):
        maxi = A.index(Amax)+1
        for i in range(N):
            if i == maxi-1:
                pass
            else:
                print(maxi,i+1)
        for i in range(N-1):
            print(i+1,i+2)
    else:
        mini = A.index(Amin)+1
        for i in range(N):
            if i == mini-1:
                pass
            else:
                print(mini,i+1)
        for i in range(N-1):
            print(N-i,N-i-1)
