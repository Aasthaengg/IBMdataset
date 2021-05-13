def sign(X):
    return [-1,0,1][(X>=0)+(X>0)]

N = int(input())
A = [int(T) for T in input().split()]

AFPCnt = 0
AFPNow = 0
for TFP in range(0,N):
    AFPNow += A[TFP]
    if sign(AFPNow)!=(-1)**TFP:
        AFPCnt += abs(AFPNow)+1
        AFPNow = (-1)**TFP

AFFCnt = 0
AFFNow = 0
for TFF in range(0,N):
    AFFNow += A[TFF]
    if sign(AFFNow)!=(-1)**(TFF+1):
        AFFCnt += abs(AFFNow)+1
        AFFNow = (-1)**(TFF+1)
print(min(AFPCnt,AFFCnt))