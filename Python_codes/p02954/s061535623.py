S = input().strip()
N = len(S)
A = [0 for _ in range(N)]
flag = 0
curR = 0
for i in range(N):
    if flag==0 and S[i]=="L":
        curL = i
        nR = i-curR
        flag = 1
    if flag==1 and S[i]=="R":
        curR = i
        nL = i-curL
        flag = 0
        if (nR+nL)%2==0:
            A[curL-1]=(nR+nL)//2
            A[curL] = (nR+nL)//2
        else:
            if nR>nL and (nR-1)%2==0:
                A[curL-1]=(nR+nL+1)//2
                A[curL] = (nR+nL)//2
            elif nR>nL and (nR-1)%2==1:
                A[curL-1]=(nR+nL)//2
                A[curL] = (nR+nL+1)//2
            elif nL>nR and (nL-1)%2==0:
                A[curL-1]=(nR+nL)//2
                A[curL]=(nR+nL+1)//2
            elif nL>nR and (nL-1)%2==1:
                A[curL-1]=(nR+nL+1)//2
                A[curL]=(nR+nL)//2
nL = N-curL
if (nR+nL)%2==0:
    A[curL-1]=(nR+nL)//2
    A[curL] = (nR+nL)//2
else:
    if nR>nL and (nR-1)%2==0:
        A[curL-1]=(nR+nL+1)//2
        A[curL] = (nR+nL)//2
    elif nR>nL and (nR-1)%2==1:
        A[curL-1]=(nR+nL)//2
        A[curL] = (nR+nL+1)//2
    elif nL>nR and (nL-1)%2==0:
        A[curL-1]=(nR+nL)//2
        A[curL]=(nR+nL+1)//2
    elif nL>nR and (nL-1)%2==1:
        A[curL-1]=(nR+nL+1)//2
        A[curL]=(nR+nL)//2
print(*A)