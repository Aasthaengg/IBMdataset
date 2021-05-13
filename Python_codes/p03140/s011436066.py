N = int(input())
A = list(input())
B = list(input())
C = list(input())
a, b, c = 0, 0, 0
cnt = 0
for i in range(N):
    if A[i] == B[i] == C[i]:
        a += 1
        b += 1
        c += 1
    elif A[i] == B[i]:
        a += 1
        b += 1
        cnt += 1
    elif B[i] == C[i]:
        b += 1
        c += 1
        cnt += 1
    elif C[i] == A[i]:
        c += 1
        a += 1
        cnt += 1
    else:
        cnt += 2
print(cnt)
