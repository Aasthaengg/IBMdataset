N = int(input())
T = [int(t) for t in input().split()]
A = [int(a) for a in input().split()]

if(T[N-1]!=A[0]):
    print(0)
    exit()

P = 1

for i in range(1,N-1):
    t = 1 if T[i-1]<T[i] else T[i]
    a = 1 if A[i]>A[i+1] else A[i]
    if(t==1):
        if(T[i]>A[i]):
            print(0)
            exit()
    if(a==1):
        if(A[i]>T[i]):
            print(0)
            exit()
    P*=min(t,a)
    P%=1000000007

print(P)