N = int(input())
A = list(map(int,input().split()))
C = [0]*N
a=0
def line(A,N):
    for i in range(N):
        C[A[i]] += 1
    if C[0] == 1:
        if N % 2==1:
            return pow(2,(N-1)//2)
        else:
            return 0
    for i in range(N):
        if C[i] != 2 and C[i]>=1:
            return 0
        elif C[i]==0:
            continue
    if N % 2 ==0:
        return pow(2,N//2)
    else:
        return pow(2,(N-1)//2)
a=line(A,N)
print(a%(pow(10,9)+7))
