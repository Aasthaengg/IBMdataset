N = int(input())
A = input()
B = input()
C = input()
cnt = 0

for i in range(N):
    if(A[i] == B[i] == C[i]):
        cnt += 0
    elif(A[i] == B[i] or C[i] == A[i] or B[i] == C[i]):
        cnt += 1
    elif(A[i] != B[i] != C[i]):
        cnt += 2
print(cnt)