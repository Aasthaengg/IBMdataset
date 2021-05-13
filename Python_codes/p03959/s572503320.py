mod = int(1e9) + 7
N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
LM = [-1 for _ in range(N)]
RM = [-1 for _ in range(N)]
LM[0] = T[0]
S = 1
for i in range(1, N):
    if T[i-1] != T[i]:
        LM[i] = T[i]
RM[-1] = A[-1]
for i in range(N, 1, -1):
    if A[i-1] != A[i-2]:
        RM[i-2] = A[i-2]
for i in range(N):
    if LM[i] != -1 and RM[i] != -1:
        if LM[i] != RM[i]:
            S *= 0
            break
    else:
        if LM[i] == -1 and RM[i] == -1:
            S *= min(T[i], A[i])
            S %= mod
        elif LM[i] != -1 and RM[i] == -1:
            if LM[i] > A[i]:
                S *= 0
                break
        elif LM[i] == -1 and RM[i] != -1:
            if RM[i] > T[i]:
                S *= 0
                break
print(S)