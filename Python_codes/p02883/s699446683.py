N,K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))

A.sort()
F.sort(reverse= True)

def det(x):
    KK = K
    for i in range(N):
        if int(max(0,A[i]-x/F[i])) == max(0,A[i]-x/F[i]):
            KK -= int(max(0,A[i]-x/F[i]))
        else:
            KK -= int(max(0,A[i]-x/F[i])) + 1
        if KK < 0:
            return False
        #print(KK)
    return True

if det(0):
    print(0)
else:
    R = [0,10**12]

    while R[1] - R[0] > 1:
        if det(int((R[0]+R[1])//2)):
            R[1] = int((R[0]+R[1])//2)
        else:
            R[0] = int((R[0]+R[1])//2)
        #print(R)

    print(R[1])#R[0]はFalse, R[1]はTrueが基本