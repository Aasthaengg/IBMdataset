N = int(input())
A = list(map(int,input().split()))

S = sum(map(abs,A))

if all([a>0 for a in A]):
    print(S-2*min(A))
    A = sorted(A)
    B = [A[0]]
    for i in range(1,N):
        B.append(B[-1]-A[i])
    for i in range(N-2):
        print(B[i],A[i+1])
    print(A[N-1],B[N-2])

elif all([a<0 for a in A]):
    print(S+2*max(A))
    A = sorted(A)
    B = [A[-1]]
    for i in range(N-1):
        B.append(B[-1]-A[i])
    for i in range(N-1):
        print(B[i],A[i])

else:
    print(S)
    A = sorted(A)
    B = [A[0]]
    for i in range(N):
        if N-1-2-i<0 or A[-2-i]<0:
            print(A[-1-i],B[-1])
            B.append(A[-1-i]-B[-1])
            break
        print(B[-1],A[-1-i])
        B.append(B[-1]-A[-1-i])
    C = [B[-1]]
    for i in range(1,N):
        if A[i]>=0:
            break
        print(C[-1],A[i])
        C.append(C[-1]-A[i])