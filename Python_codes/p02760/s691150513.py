A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
N = int(input())

D = [int(input()) for j in range(N)]
D = list(set(D))


for i in range(len(D)):
    if D[i] == A[0]:
        A[0] = -1
    elif D[i] == A[1]:
        A[1] = -1
    elif D[i] == A[2]:
        A[2] = -1
    elif D[i] == B[0]:
        B[0] = -1
    elif D[i] == B[1]:
        B[1] = -1
    elif D[i] == B[2]:
        B[2] = -1
    elif D[i] == C[0]:
        C[0] = -1
    elif D[i] == C[1]:
        C[1] = -1
    elif D[i] == C[2]:
        C[2] = -1
    else:
        continue
    



if (A[0] == -1 and A[1] == -1 and A[2] == -1)or(B[0] == -1 and B[1] == -1 and B[2] == -1)or(C[0] == -1 and C[1] == -1 and C[2] == -1)or(A[1] == -1 and B[1] == -1 and C[1] == -1)or(A[0] == -1 and B[0] == -1 and C[0] == -1)or(A[2] == -1 and B[2] == -1 and C[2] == -1)or(A[0] == -1 and B[1] == -1 and C[2] == -1)or(A[2] == -1 and B[1] == -1 and C[0] == -1):
    print('Yes')
else:
    print('No')