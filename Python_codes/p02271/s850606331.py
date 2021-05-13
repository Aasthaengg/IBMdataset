N=int(input())
L=list(map(int,input().split()))
B=1
for i in range(N):
    B=B|B<<L[i]
BI=list(str(bin(B)))
BI=BI[2:]
SB=BI[::-1]
#print(SB)
Q=int(input())
A=list(map(int,input().split()))
for i in range(Q):
    if A[i]>=len(SB):
        print("no")
    elif SB[A[i]]=="1":
        print("yes")
    else:
        print("no")
